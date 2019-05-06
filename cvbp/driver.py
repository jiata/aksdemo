import timeit as t
import logging
import os
from azureml.core.model import Model
from fastai.vision import open_image, load_learner
from azureml.contrib.services.aml_request import rawhttp
from azureml.core.model import Model
from toolz import compose


def _create_scoring_func():
    """ Initialize ResNet 18 Model
    """
    logger = logging.getLogger("model_driver")
    start = t.default_timer()
    model_name = "resnet_model"
    model_path = Model.get_model_path(model_name=model_name)
    model_dir_path, model_filename = os.path.split(model_path)
    model = load_learner(path=model_dir_path, fname=model_filename)
    end = t.default_timer()

    loadTimeMsg = "Model loading time: {0} ms".format(round((end - start) * 1000, 2))
    logger.info(loadTimeMsg)

    def call_model(img_ref):
        img = open_image(img_ref)
        pred_class, pred_idx, outputs = model.predict(img)
        decoded_predictions = [str(pred_class), outputs[pred_idx].item()]
        return [decoded_predictions]

    return call_model


def get_model_api():
    logger = logging.getLogger("model_driver")
    scoring_func = _create_scoring_func()

    def process_and_score(images_dict):
        """ Classify the input using the loaded model
        """
        start = t.default_timer()
        logger.info("Scoring {} images".format(len(images_dict)))
        preds = {key: scoring_func(img_ref) for key, img_ref in images_dict.items()}
        end = t.default_timer()

        logger.info("Predictions: {0}".format(preds))
        logger.info("Predictions took {0} ms".format(round((end - start) * 1000, 2)))
        return (preds, "Computed in {0} ms".format(round((end - start) * 1000, 2)))

    return process_and_score


def init():
    """ Initialise the model and scoring function
    """
    global process_and_score
    process_and_score = get_model_api()


@rawhttp
def run(request):
    """ Make a prediction based on the data passed in using the preloaded model
    """
    return process_and_score(request.files)

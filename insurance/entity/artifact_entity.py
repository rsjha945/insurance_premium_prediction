from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact",
                                ["train_file_path","test_file_path","is_generated","message"])

DataValidationArtifact = namedtuple("DataValidationArtifact",
["schema_file_path","report_file_path","report_page_file_path","is_validated","message"])

DataTransformationArtifact = namedtuple("DataTransformationArtifact",["is_Transformed","transformed_train_path","transformed_test_path","preprocessed_pkl_path","message"])

ModelTrainerArtifact = namedtuple("ModelTrainerArtifact", ["is_trained", "message", "trained_model_file_path",
                                                           "train_rmse", "test_rmse", "train_accuracy", "test_accuracy",
                                                           "model_accuracy"])

ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact", ["is_model_accepted", "evaluated_model_path"])

ModelPusherArtifact = namedtuple("ModelPusherArtifact", ["is_model_pusher", "export_model_file_path"])
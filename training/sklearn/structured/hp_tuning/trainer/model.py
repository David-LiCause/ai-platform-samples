# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""ML model definitions."""

from sklearn import ensemble


def get_estimator(arguments):
    """Generate ML Pipeline which include both pre-processing and model training

    Args:
      arguments: (argparse.ArgumentParser), parameters passed from command-line

    Returns:
      structured.pipeline.Pipeline
    """

    # n_estimators and max_depth are expected to be passed as
    # command line argument to task.py
    classifier = ensemble.RandomForestClassifier(
        max_depth=arguments.max_depth,
        min_samples_split=arguments.min_samples_split,
        criterion=arguments.criterion,
    )

    return classifier

import unittest
import os

from analysis import BehavioralSubjective, BehavioralBrain, BrainActivationAnalysis
from config import ROOT_DIR

OUTPUT_DIR = ROOT_DIR + '/analysis/output'


def empty_output_dir():
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".pdf")]
    for file in files:
        os.remove(os.path.join(OUTPUT_DIR, file))


def get_number_of_files_in_output():
    path, dirs, files = next(os.walk(OUTPUT_DIR))
    file_count = len(files)
    return file_count


class PipelineTest(unittest.TestCase):
    def test_behavioral_subjective(self):
        empty_output_dir()

        file_count_initial = get_number_of_files_in_output()
        self.assertEqual(1, file_count_initial)  # only .gitkeep file

        BehavioralSubjective.main()
        file_count_end = get_number_of_files_in_output()
        self.assertEqual(75, file_count_end)  # pipeline should create 74 files + .gitkeep

    def test_behavioral_brain(self):
        empty_output_dir()

        file_count_initial = get_number_of_files_in_output()
        self.assertEqual(1, file_count_initial)  # only .gitkeep file

        BehavioralBrain.main()
        file_count_end = get_number_of_files_in_output()
        self.assertEqual(13, file_count_end)  # pipeline should create 12 files + .gitkeep

    def test_brain_activation(self):
        empty_output_dir()

        file_count_initial = get_number_of_files_in_output()
        self.assertEqual(1, file_count_initial)  # only .gitkeep file

        BrainActivationAnalysis.main()
        file_count_end = get_number_of_files_in_output()
        self.assertEqual(211, file_count_end)  # pipeline should create 210 files + .gitkeep


if __name__ == '__main__':
    unittest.main()

import importlib
import os
import sys
# let's test modules import from the code_folder
sys.path.insert(1, "../code_folder")
sys.path.insert(1, "code_folder")


def main():
    files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    modules = []
    # Grabbing all the test files names
    for i in files:
        if i.startswith("test_") and i.endswith(".py") and i != "test_runner.py":
            modules.append(i[:-3])

    # Importing the testing classes
    classes = []
    for module in modules:
        thing = importlib.import_module(module)
        class_name = module.replace("_", " ").title().replace(" ", "")
        classes.append(getattr(thing, class_name))

    # Running the tests and recording results
    failures = 0
    successes = 0
    for i_class in classes:
        thing = i_class()
        success, failure = thing.run_test()
        failures += failure
        successes += success

    print("Ran a total of {} tests\033[92m {} successe(s)\033[00m and\033[91m {} failure(s)\033[00m".format(
        successes + failures, successes, failures))

    return failures


if __name__ == '__main__':
    main()

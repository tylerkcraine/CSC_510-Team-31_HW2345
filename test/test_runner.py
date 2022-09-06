import importlib
import os
import sys
# let's test modules import from the code_folder
sys.path.insert(1, "../code_folder")

def main():
    files = os.listdir()
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
    for i_class in classes:
        thing = i_class()
        thing.run_test()


if __name__ == '__main__':
    main()
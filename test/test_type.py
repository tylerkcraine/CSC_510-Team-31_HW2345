import traceback

class TestType(object):
    def run_test(self):
        failures = 0
        successes = 0
        methods = dir(self)
        test_methods = []
        for method in methods:
            if method.startswith("test_"):
                test_methods.append(method)
        for test_method in test_methods:
            test_thing = getattr(self,test_method)
            print("Running " + test_method)
            try:
                test_thing()
                print("\033[92m {}\033[00m" .format("SUCCESS!!"))
                successes += 1
            except Exception as e:
                traceback.print_exc()
                print("\033[91m {}\033[00m" .format("FAILED"))
                failures += 1
            print()

        return successes, failures

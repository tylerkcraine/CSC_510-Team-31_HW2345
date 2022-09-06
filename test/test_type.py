class TestType(object):
    def run_test(self):
        failures = 0
        methods = dir(self)
        test_methods = []
        for method in methods:
            if method.startswith("test_"):
                test_methods.append(method)
        for test_method in test_methods:
            test_thing = getattr(self,test_method)
            print("Running " + test_method, end="")
            try:
                test_thing()
                print("\033[92m {}\033[00m" .format("SUCCESS!!"))
            except:
                print("\033[91m {}\033[00m" .format("FAILED"))
                failures += 1

        return failures

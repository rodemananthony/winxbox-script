import test_test

path = 'data.json'

script = test_test.TestTest()
script.setup_method()
script.load_vars(path)

script.test_verify()

script.teardown_method()
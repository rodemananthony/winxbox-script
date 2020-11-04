import test_test

path = 'data.json'

wait = 15*60 - 4    # time in seconds
print('starting')
script = test_test.TestTest()
script.setup_method()
script.load_vars(path)

script.test_test(wait)

script.teardown_method()
print('done')
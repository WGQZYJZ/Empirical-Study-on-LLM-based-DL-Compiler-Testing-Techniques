
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.full([x1.size(1)], 1, dtype=torch.float32, device=device)
        t2 = convert_element_type(t1, torch.float64)
        t3 = torch.cumsum(t2, 1)
        return None


# Initializing the model
m = Model()
x = torch.randn(10, 5, 16, 16)


def __create_testcase__():
    x = torch.ones([1, 3, 64, 64])

    __call__model__(m, x)


# Inputs to the model
x1 = __gen_input__(m, x)
if (__output__.dtype != x1.dtype or __output__.shape != x1.shape):
    __error__(True, 'The output shape {} and dtype {} should be the same as the input shape {} and dtype {}'.format(__output__.shape, __output__.dtype, x1.shape, x1.dtype))
__testcase_check__(__create_testcase__)
# The test case checks that the output of __call__model__ equals to the generated tensor


def __create_testcase__():
    x = torch.randn([1024], dtype=torch.float32)

    __call__model__(m, x)


# Inputs to the model
x1 = __gen_input__(m, x)
if (__output__.dtype != x1.dtype or __output__.shape != x1.shape):
    __error__(True, 'The output shape {} and dtype {} should be the same as the input shape {} and dtype {}'.format(__output__.shape, __output__.dtype, x1.shape, x1.dtype))
__testcase_check__(__create_testcase__)
# The test case checks that the output of __call__model__ equals to the generated tensor


def __create_testcase__():
    x = torch.ones([64], dtype=torch.int32)

    __call__model__(m, x)


# Inputs to the model
x1 = __gen_input__(m, x)
if (__output__.dtype != x1.dtype or __output__.shape != x1.shape):
    __error__(True, 'The output shape {} and dtype {} should be the same as the input shape {} and dtype {}'.format(__output__.shape, __output__.dtype, x1.shape, x1.dtype))
__testcase_check__(__create_testcase__)
# The test case checks that the output of __call__model__ equals to the generated tensor


def __create_testcase__():
    x = torch.randn([32, 64], dtype=torch.float64)

    __call__model__(m, x)


# Inputs to the model
x1 = __gen_input__(m, x)
if (__output__.dtype != x1.dtype or __output__.shape != x1.shape):
    __error__(True, 'The output shape {} and dtype {} should be the same as the input shape {} and dtype {}'.format(__output__.shape, __output__.dtype, x1.shape, x1.dtype))
__testcase_check__(__create_testcase__)
# The test case checks that the output of __call__model__ equals to the generated tensor


def __create_testcase__():
    x = torch.randn([32, 64], dtype=torch.float32)

    __call__model__(m, x)


# Inputs to the model
x1 = __gen_input__(m, x)
if (__output__.dtype != x1.dtype or __output__.shape != x1.shape):
    __error__(True, 'The output shape {} and dtype {} should be the same as the input shape {} and dtype {}'.format(__output__.shape, __output__.dtype, x1.shape, x1.dtype))
__testcase_check__(__create_testcase__)
# The test case checks that the output of __call__model__ equals to the generated tensor


def __create_testcase__():
    x = torch.randn([256], dtype=torch.float32)

    __call__model__(m, x)


# Inputs to the model
x1 = __gen_input__(m, x)
if (__output__.dtype != x1.dtype or __output__.shape != x1.shape):
    __error__(True, 'The output shape {} and dtype {} should be the same as the input shape {} and dtype {}'.format(__output__.shape, __output__.dtype, x1.shape, x1.dtype))
__testcase_check__(__create_testcase__)
# The test case checks that the output of __call__model__ equals to the generated tensor


def __create_testcase__():
    x = torch.randn([32], dtype=torch.int64)

    __call__model__(m, x)


# Inputs to the model
x1 = __gen_input__(m, x)
if (__output__.dtype != x1.dtype or __output__.shape != x1.shape):
    __error__(True, 'The output shape {} and dtype {} should be the same as the input shape {} and dtype {}'.format(__output__.shape, __output__.dtype, x1.shape, x1.dtype))
__testcase_check__(__create_testcase__)
# The test case checks that the output of __call__model__ equals to the generated tensor
## ## ## ## ## ## ## ##


} // namespace

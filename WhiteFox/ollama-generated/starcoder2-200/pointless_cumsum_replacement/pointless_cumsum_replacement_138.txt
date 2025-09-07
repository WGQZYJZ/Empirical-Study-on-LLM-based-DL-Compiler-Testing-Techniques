
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, arg1, arg2, dtype=None):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype)
        v2 = torch.ops._internal.convert_element_type(v1, dtype)
        v3 = torch.ops._internal.cumsum(v2, dim=1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(10, 5)
arg1  = x1.shape[0] + x1.shape[0]*int((torch.randint(-2147483647, 2147483647).tolist() % ((x1.shape[0] * int(136))) + 1)/int(1))
arg2  = x1.shape[1] / 9543
dtype  = torch._C._get_default_dtype() # 16 bit float
 

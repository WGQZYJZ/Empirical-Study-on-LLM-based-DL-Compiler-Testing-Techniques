
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cumsum = torch.nn.functional.linear
 
    def forward(self, x1, arg1, arg2):
        v1  = torch.full([arg1, arg2], 1) 
        v2  = v1.to('cpu')
        v3  = v2 + torch.cumsum(v2, 0)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
arg1, arg2 = [64], [64]
x1 = torch.randn(1, 512 * 64 ** 2).to('cpu')
__output__  = m(x1)


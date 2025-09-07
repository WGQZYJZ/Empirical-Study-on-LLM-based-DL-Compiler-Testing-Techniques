
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2=None):
        v1 = torch.mm(inp1, inp2) 
        v2 = v1 + inp  # 'v1' is an input tensor and 'inp' is a keyword argument
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(640, 5)
x2 = torch.randn(3840, 5)
__output__  = m(x1, x2=None)  # 'x2' is not passed as a keyword argument


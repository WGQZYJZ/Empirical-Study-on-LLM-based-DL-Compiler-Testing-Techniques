
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v2 = torch.mm(x1, 3) + inp if type(inp) is not None else 0.5 * torch.mm(x1, 3) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model: input tensor and keyword argument value for the input tensor
x1 = torch.randn(4, 8)
inp_value = torch.randn(8, 5)

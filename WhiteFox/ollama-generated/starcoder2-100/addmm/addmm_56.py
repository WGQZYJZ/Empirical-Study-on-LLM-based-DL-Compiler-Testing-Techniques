
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v1 = torch.mm(x1, x2)  # Matrix multiplication on two input tensors
        v2 = v1 + inp  # Add the result of matrix multiplication to another tensor 'inp'
        return v2


# Initializing the model
m = Model()
inp  = torch.randn(480, 360)

# Inputs to the model
x1  = torch.randn(357948, 360)
x2  = torch.randn(360, 640)


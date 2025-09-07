
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):  # The model takes two input tensors as inputs
        v0 = torch.cat([x1] * len([x2]), dim=0)
        return v0


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8, 3, 64, 64)
x2  = torch.randn(1, 3, 5, 5)
__output__   = m(x1, x2)

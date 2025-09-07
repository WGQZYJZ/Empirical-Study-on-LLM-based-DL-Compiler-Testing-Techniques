
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.zeros((32,))  # Initialize a random tensor of size (32,) to hold an arbitrary value
        v1 = linear(x1) + v 
        return v1


# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(4, 50)
__output__= m(x1)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x2):
        v1  = self.linear(x2) # Apply linear transformation to the input tensor
        v2  = v1 - 0.9 
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
__input__ = torch.randn(3, 784)
__output__  = m(__input__)
 
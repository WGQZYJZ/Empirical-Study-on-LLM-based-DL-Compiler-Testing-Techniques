
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 5)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + other 
        v3 = F.relu(v2) 
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
    x1  = torch.randn(8, 64)
 
 ## This is an optional part which will be used to test different inputs and other keyword arguments.
    other  = F.relu(x1)
 
  # Passing the keyword argument `other` as another input.
    __output__   = m(x1=x1, other=other)


# References
- [PyTorch Documentation - Modules](https://pytorch.org/docs/stable/nn.html?highlight=nn%20module#torch-nn-modules)

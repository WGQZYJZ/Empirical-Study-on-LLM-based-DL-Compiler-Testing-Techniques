
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1, other=None): 
        v0 = self.linear(x1)  
        v1 = v0 + other
        return v1

# Initializing the model with keyword argument "other" set to another tensor.
m = Model()
# Inputs to the model
x2  = torch.randn(3, 32)


# Inputs to the model
x4  = torch.randn(3, 32)

 # Inputs to the model
x5  = torch.randn(3, 32)

__output__1  = m(x2, other=torch.tensor(-0.789))
__output__2  = m(x4)
__output__3  = m(x5, other=-0.673+other)


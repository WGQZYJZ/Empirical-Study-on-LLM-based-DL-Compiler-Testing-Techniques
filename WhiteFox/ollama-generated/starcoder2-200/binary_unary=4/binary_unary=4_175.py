
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3,16)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other
        v3  = F.relu(v2) 
        return v3


# Initializing the model
m = Model()
 
other_tensor = torch.randn(100,) # Dummy input tensor to be passed as a keyword argument to linear transformation.

# Inputs to the model
x  = torch.randn(64, 3)
__output__  = m(x)


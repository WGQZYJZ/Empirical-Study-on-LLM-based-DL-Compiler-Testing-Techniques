
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x2):
        v0 = self.linear(x2) # Apply a linear transformation to the input tensor
        return v0
 
# Initializing the model
m = Model()


# Inputs to the model
x2  = torch.randn(8,) 

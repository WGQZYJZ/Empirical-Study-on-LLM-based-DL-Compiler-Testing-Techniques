
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(3072, 10)
 
    def forward(self, x):
        v1  = self.lin(x) # Apply a linear transformation to the input tensor
        v2  = v1 + 3 # Add 3 to the output of the linear transformation
        v3  = torch.clamp_min(v2, 0) # Clamp the output of the addition operation to a minimum of 0
        v4  = torch.clamp_max(v3, 6) # Clamp the output of the previous operation to a maximum of 6
        return v4 / 6


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1024, 3072)

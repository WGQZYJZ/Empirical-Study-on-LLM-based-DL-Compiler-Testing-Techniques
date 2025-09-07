
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x1): 
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor

        return torch.clamp_min(v1, -75).clamp_max(v1, +64)  # Clamp both the minimum and maximum values


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2000, 1*1938*3957)

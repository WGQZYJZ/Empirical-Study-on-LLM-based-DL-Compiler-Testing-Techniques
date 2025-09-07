
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.clamp_min(v1, -5.96046e-8) # Apply a linear transformation to the input tensor
        v3 = torch.clamp_max(v2, 5.96046e-8) # Clamp the output of the linear transformation to a maximum value
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 10)

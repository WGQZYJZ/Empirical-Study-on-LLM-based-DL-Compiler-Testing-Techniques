
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 1000)
 
    def forward(self, x):
        v1 = self.linear(x)
        v3 = v1 / 6 + 3
        v4 = torch.clamp(min=0, max=v3 - 3) # clamp is actually not required here since we are clamping between min and max but it is good practice to include it for readability.
        v5 = v1 * v4
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
x  = torch.randn(32, 128)
__output__  = m(x)


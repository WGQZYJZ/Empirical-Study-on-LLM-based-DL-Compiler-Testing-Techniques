
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + 3 # Addition operation
        v3  = v2 * 6  # Multiplication by 6
        v4  = torch.clamp_max(v3, 0)  # Clamp to the maximum of 0
        v5  = torch.clamp_min(v4, 10)  # Clamps to the minimum of 10 
        v6  = v5 / 10  # Divide by 10
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 128)
__output__  = m(x1)



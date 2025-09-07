
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).to(torch.float32) # Convert to float32 before multiplication to ensure the model is different from the previous one.
        v3 = v1 * negative_slope
        return torch.where(v2, v1, v3)


# Initializing the model
m  = Model()
negative_slope = 0.5

# Inputs to the model
x1 = torch.randn(4, 16)
__output__= m(x1)
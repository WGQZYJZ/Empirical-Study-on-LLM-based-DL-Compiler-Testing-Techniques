
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * negative_slope
        v3 = torch.where(v1, v2, x1) # Note that the input tensor has already been multiplied by a negative slope
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 16, 64) * 0.5

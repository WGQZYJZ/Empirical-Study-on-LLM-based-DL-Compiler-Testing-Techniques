
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128 * 64, 3)
 
    def forward(self, x1):
        v0 = self.linear(x1)
        v1 = v0 > 0
        v2 = v0 * negative_slope
        v3 = torch.where(v1, v0, v2)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
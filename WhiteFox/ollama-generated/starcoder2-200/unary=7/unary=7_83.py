
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * clamp(min=0, max=6, v1 + 3) # Clamp the output of linear transformation
        v3 = v2 / 6
        return v3

# Initializing model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8)

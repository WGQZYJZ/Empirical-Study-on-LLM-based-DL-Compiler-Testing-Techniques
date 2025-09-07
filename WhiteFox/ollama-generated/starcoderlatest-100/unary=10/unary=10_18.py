
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 3 # Add 3 to the output of the linear transformation
        v2 = torch.clamp_min(v1, 0) # Clamp the output of the addition operation to a minimum of 0
        v3 = torch.clamp_max(v2, 6) # Clamp the output of the previous operation to a maximum of 6
        v4 = v3 / 6 # Divide the output of the previous operation by 6
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

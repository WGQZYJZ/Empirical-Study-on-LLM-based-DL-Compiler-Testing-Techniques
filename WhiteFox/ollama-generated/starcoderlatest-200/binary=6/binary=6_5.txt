
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1, other=0.0):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

 # Apply different values to 'other' for two different scenarios
 other_vals = [0.0, 1.0]
 for v in other_vals:
     
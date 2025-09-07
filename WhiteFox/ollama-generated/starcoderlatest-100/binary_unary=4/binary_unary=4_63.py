
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other is not None:
            v2 = v1 + other
        else:
            return v1
        v3 = torch.relu(v2)
        return v3


# Initializing the model and defining keyword arguments
m  = Model()
other_tensor = torch.randn(8)

# Inputs to the model with defined keyword arguments
x1  = torch.randn(1, 3, 64, 64)

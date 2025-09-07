
class Model(torch.nn.Module):
    def __init__(self, min_value: int = -100, max_value: int = 100):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp(v1, min=min_value, max=max_value)
        return v2

# Initializing the model with a minimum and maximum value
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 
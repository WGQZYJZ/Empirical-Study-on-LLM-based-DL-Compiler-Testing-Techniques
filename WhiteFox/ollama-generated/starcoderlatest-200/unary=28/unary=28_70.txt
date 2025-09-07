
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=0)
        v3 = torch.clamp_max(v2, max_value=64)
        return v3


# Initializing the model and providing values of minimum and maximum for each clamp operation
m = Model()
min_value 0, max_value 64

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)

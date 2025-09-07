
class Model(torch.nn.Module):
    def __init__(self, min_value=1, max_value=3):
        super().__init__()
        self.linear = torch.nn.Linear(8, 64)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x2, min_value=0, max_value=2):
        v2 = self.linear(x2)
        v3 = torch.clamp(v2, min_value, max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x2  = torch.randn(1, 8)

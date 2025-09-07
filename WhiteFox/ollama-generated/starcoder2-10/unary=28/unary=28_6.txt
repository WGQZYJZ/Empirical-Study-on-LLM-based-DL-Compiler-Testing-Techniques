
class Model(torch.nn.Module):
    def __init__(self, min_value = -0.12345678910, max_value = 1.234567891011):
        super().__init__()
        self.linear = torch.nn.Linear(123, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=min_value)
        v3 = torch.clamp_max(v2, max=max_value)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
 x1  = torch.randn(1, 4)
 
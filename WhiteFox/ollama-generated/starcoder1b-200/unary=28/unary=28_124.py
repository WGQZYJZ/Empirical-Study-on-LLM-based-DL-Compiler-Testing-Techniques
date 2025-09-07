
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1.0):
        super().__init__()
        self.linear = torch.nn.Linear(8, 3)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x):
        v  = self.linear(x)
        v = v.clamp(min=self.min_value, max=self.max_value)
        return v

# Initializing the model
m = Model(0, 1.0)

 # Inputs to the model
x = torch.randn(1, 3)

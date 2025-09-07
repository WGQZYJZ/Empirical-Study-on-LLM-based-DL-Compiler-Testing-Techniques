
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)
 
    def forward(self, x1, min_value=0.0, max_value=5.0):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 20)
min_value = -3.141592653589793
max_value = 2.344200266542563

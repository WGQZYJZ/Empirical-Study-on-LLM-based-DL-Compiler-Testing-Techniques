
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-5, max_value=3e5):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=32, out_features=16)
 
    def forward(self, x):
        v  = self.linear(x)
        v = torch.clamp_min(v, min_value)
        v = torch.clamp_max(v, max_value)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32) # x1 = (64,64)

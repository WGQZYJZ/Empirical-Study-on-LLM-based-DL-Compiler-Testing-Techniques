
class Model(torch.nn.Module):
    def __init__(self, min_value=0.5, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model with min and max values for clamping
m = Model(min_value=0.5, max_value=1.5)


# Inputs to the model with clamped input tensor.
x1 = torch.randn(1, 8, 64) * 2 - 1




class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.shape[0], -1))
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model(max_value=15)  # `0` is also a valid keyword argument


# Inputs to the model
x1 = torch.randn(1, 64*64, requires_grad=True)

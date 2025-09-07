
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 128)
 
    def forward(self, x):
        v1 = self.linear(x.view(-1))
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model(min_value=0, max_value=1)

# Inputs to the model
x = torch.randn(4, 64 * 64)

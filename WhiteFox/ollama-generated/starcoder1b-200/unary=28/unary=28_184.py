
class Model(torch.nn.Module):
    def __init__(self, min_value=0.01, max_value=0.99):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 3 * 3, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1).view(-1, 3, 32, 32)
        v2 = torch.clamp_min(v1, min_value).view(
            -1, 64, 64, 128).contiguous()
        v3 = torch.clamp_max(v2, max_value).view(-1, 64 * 3, 128)
        return v3


# Initializing the model
m = Model(min_value=0.0, max_value=0.9)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

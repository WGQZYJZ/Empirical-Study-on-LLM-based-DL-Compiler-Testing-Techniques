
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, -0.5, True)
        v3  = torch.clamp_max(v2, 0.5, False)
        return v3

# Initializing the model
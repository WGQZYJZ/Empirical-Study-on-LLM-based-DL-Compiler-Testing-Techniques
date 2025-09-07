
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t3 = torch.clamp_max(torch.clamp_min(x1), 0)
        return t3

# Initializing the model
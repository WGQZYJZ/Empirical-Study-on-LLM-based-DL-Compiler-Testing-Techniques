
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = x1.permute(0, 2)
        v3a = torch.nn.functional.linear(v1, 1.) # v3a, v4a is not used.
        return [v3a]

# Initializing the model
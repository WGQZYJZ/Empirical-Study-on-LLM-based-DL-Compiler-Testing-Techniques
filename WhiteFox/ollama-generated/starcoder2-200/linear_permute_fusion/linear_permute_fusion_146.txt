
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1)
        v2  = v.permute(0, 2, 1)
        return v2

# Initializing the model

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        x = torch.nn.Linear(32, 64)(x)
        out = x + torch.ones([50, 8])
        return out

# Initializing the model
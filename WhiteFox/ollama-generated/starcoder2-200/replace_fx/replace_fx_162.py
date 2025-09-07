
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.dropout(x1, 0.5)
        return torch.rand_like(v)


# Initializing the model
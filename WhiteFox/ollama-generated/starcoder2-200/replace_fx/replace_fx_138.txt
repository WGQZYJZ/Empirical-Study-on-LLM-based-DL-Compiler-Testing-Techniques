
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.dropout(x1, 0.8)
        v2 = torch.rand_like(v3, dtype=v3.dtype)
        return v2


# Initializing the model
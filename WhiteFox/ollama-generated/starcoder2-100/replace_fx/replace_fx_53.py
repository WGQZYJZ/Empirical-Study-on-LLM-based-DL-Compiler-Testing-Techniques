
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3  = torch.nn.functional.dropout(x1, 0.5)
        v4  = torch.rand_like(v3)

        return v4


# Initializing the model
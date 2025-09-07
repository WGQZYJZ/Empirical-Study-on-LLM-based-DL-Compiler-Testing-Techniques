
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v2 = torch.nn.functional.dropout(x1, 0.5)
        v3 = torch.rand_like(v2, device='cpu')
        return v2


# Initializing the model
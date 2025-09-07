
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1  = torch.nn.functional.linear(x1)
        v2  = torch.bmm(y1, v1)
        return v2


# Initializing the model
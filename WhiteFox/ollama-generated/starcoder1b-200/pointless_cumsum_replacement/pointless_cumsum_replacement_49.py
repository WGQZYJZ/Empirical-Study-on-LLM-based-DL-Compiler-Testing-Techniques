
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2):
        v1 = torch.full([arg1, arg2], 1, dtype=torch.float32, layout='auto', device='cpu')
        v2 = torch.cumsum(v1, dim=1)
        return v2


# Initializing the model
m = Model()





class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       return torch.split(x1, 2048)
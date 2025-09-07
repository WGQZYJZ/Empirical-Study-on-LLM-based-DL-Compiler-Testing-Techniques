class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v0 = torch.sin(x1)
        v2 = torch.cos(v0)
        return v2

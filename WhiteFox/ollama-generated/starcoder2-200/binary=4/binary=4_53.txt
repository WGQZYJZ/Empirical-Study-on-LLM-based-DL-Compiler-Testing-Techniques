
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v1 = torch.nn.Linear(x1)
        v2 = v1 + other
        return v2


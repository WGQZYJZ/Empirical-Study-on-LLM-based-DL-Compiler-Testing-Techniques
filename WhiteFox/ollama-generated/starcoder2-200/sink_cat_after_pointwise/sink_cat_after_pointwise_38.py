
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.relu(x1)
        v3  = v2 + x1 
        return v3


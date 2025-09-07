
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.bmm(x1, self) # Permute x1 and the model itself
        return v3


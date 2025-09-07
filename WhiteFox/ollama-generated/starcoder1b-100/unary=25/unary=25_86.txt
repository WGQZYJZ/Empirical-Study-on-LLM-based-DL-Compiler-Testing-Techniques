
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = (v1 > 0).float()
        v3 = v1 * (-1.56285367210255 + (1 / 12).log() - (4 * 1e-5).reciprocal())
        v4 = torch.where(v2, x1, v3)
        return v4


# Initializing the model
m = Model()

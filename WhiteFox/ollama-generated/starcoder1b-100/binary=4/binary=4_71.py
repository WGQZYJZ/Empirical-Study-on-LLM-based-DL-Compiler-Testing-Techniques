
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear1 = torch.nn.Linear(dim, 8)
        self.linear2 = torch.nn.Linear(8, 3)
 
    def forward(self, x1, other=None):
        v1 = self.linear1(x1)
        if isinstance(other, int):
            v2 = x1 + torch.randn_like(x1) * other
        else:
            v2 = self.linear2(other)
        return v2


# Initializing the model
m = Model(3)


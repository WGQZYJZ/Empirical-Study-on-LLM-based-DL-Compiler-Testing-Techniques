
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.layer(x1) * 0.5
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 + 1
        v5 = v2 * v4
        return self.layer(v5)


# Initializing the model
m = Model()


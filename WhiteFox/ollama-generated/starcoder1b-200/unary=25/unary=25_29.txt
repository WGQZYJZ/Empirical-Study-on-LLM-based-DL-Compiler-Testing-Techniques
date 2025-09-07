
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, -v1 * 0.5)
        v3 = torch.mul(v1, v2)
        return v3


# Initializing the model
m = Model()


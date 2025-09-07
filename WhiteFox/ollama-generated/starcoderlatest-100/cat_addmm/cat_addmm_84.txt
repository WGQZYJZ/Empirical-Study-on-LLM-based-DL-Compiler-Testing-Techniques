
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.addmm = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1, x2):
        v1 = self.addmm(x1 * x2)
        v2 = torch.cat([v1], dim=dim)
        return v2
# Initializing the model
m = Model(1)



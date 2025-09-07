
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = v1 + torch.addmm(v1, mat1, mat2)
        v3 = torch.cat([v1, v2], dim=0)
        return v3


# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)

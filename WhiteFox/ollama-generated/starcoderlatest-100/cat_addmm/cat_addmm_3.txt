
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 8)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = self.linear2(v1)
        t1 = torch.addmm(v2, mat1, mat2)
        t2 = torch.cat([t1], dim=dim)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(64, 3, 64, 64)

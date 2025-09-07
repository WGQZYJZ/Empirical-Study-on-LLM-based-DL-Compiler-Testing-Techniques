
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1, x2, dim):
        v1 = torch.addmm(x1, x2, x2)
        v2 = torch.cat([v1], dim)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(4, 3, 64, 64)
dim = 0 # 0 indicates a column while -1 indicates a row

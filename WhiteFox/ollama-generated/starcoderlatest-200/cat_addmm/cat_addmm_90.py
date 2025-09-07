
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.eye(8, dtype=torch.float32).to(dtype="float")
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, x1)
        v2 = torch.cat([v1], dim=1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64).to(dtype="float")

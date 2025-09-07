
class Model(torch.nn.Module):
    def __init__(self, out_features: int):
        super().__init__()
        self.fc = torch.nn.Linear(40, 20)
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim=1)
        return self.fc(v2)


# Initializing the model
m = Model(out_features=30)

# Inputs to the model
x1 = torch.randn(1, 40)
mat1 = torch.randn(80, 40)
mat2 = torch.randn(60, 40)

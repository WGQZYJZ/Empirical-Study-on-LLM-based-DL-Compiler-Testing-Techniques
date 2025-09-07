
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(256, 4096)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = torch.addmm(v1, mat1, mat2)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

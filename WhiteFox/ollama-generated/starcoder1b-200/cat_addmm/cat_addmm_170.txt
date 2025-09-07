
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(8, 1)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)
        return torch.cat([v1], dim)


# Initializing the model
m = Model()



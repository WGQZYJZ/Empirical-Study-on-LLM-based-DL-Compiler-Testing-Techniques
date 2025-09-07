
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1  = torch.nn.Linear(576, 40)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2) 
        return torch.cat([v1], dim=3)


# Initializing the model
m = Model()


# Inputs to the model
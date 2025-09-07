
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(24, 3)
 
    def forward(self, x1):
        v1  = self.lin1(x1)
        return torch.addmm(v1, mat1, mat2).squeeze()
 

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(3072)

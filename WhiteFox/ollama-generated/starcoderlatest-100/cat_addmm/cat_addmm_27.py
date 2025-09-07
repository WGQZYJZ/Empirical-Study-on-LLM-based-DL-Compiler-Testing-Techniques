
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        t1 = torch.addmm(x1, mat1, mat2)
        t2 = torch.cat([t1], dim)
        return t2
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1024, 64, 3, 64)

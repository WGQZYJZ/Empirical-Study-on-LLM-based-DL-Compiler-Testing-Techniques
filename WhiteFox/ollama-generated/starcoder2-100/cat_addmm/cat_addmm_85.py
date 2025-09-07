
class Model(torch.nn.Module):
    def __init__(self, dim = 2):
        super().__init__()
        self.dim = dim
        self.fc1  = torch.nn.Linear(3 * 64 * 64, 8)
        self.fc2  = torch.nn.Linear(8, 9)
 
    def forward(self, x1):
        v1  = torch.reshape(x1, ( -  1 ,   3))
        v2  = self.fc1(v1)
        v3  = self.fc2(v2) 
        return torch.cat([v3], dim=self.dim)


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(8, 64 * 64 , 3)
__output__  = m(x1)
 

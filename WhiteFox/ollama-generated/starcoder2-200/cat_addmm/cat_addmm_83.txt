
class Model(torch.nn.Module):
    def __init__(self, n1=256):
        super().__init__()
        self.fc  = torch.nn.Linear(3*320*48+n1, 3)
 
    def forward(self, x1, x2, x3): 
        v1  = torch.flatten(x1, start_dim=1)
        v2  = torch.flatten(x2, start_dim=1)
        v3  = torch.flatten(x3, start_dim=1)
        t1  = torch.addmm(v1, mat1, mat2)
        t2  = torch.cat([t1], dim=1) 
        t4  = self.fc(t3).relu() 
        return t5

# Initializing the model
m = Model()


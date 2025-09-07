
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.split(x1, 4, dim=0)
        t2 = torch.split(x2, 4, dim=0)
        t3 = torch.cat([t1[i] for i in range(len(t1))], dim=0) 
        return t3

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 8, 256, 256)
x2 = torch.randn(1, 8, 64, 64)

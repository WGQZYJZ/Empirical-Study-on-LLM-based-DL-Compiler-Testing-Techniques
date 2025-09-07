
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, size=1024):
        t1 = torch.cat([x1, x2], dim=1)
        t2 = t1[:, 0:size]
        t3 = t2[:, 0:size]
        t4 = torch.cat([t1, t3], dim=1)
        return t4
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 16, 1024)
x2 = torch.randn(1, 8, 1024)
x3 = torch.randn(1, 4, 1024)

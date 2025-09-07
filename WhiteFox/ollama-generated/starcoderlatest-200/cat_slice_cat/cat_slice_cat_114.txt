
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, size):
        t2 = t1[:, 0:size]
        return torch.cat([t1, t2], dim=1)

 # Initializing the model
m = Model()

 # Inputs to the model
t1 = torch.randn(4, 3, 64, 64)
size = int(1e+10) * 1e-5

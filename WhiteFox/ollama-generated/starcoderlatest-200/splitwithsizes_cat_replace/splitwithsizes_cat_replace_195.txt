
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.split(x1, 3, dim=0)
        t2 = torch.cat([t1[i] for i in range(len(t1))], dim=0)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

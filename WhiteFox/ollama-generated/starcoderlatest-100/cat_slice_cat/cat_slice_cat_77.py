
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1):
        v1 = torch.cat([t1[:, i:i+size] for i in range(0, len(t1), size)], dim=1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = x1[:, 0:5]

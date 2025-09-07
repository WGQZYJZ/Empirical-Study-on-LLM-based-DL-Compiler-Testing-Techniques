
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, t2, size):
        v1 = torch.cat([t1, t2], dim=1)
        v2 = v1[:, 0:size]
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(5, 3, 64, 64)
size = x1.shape[1]

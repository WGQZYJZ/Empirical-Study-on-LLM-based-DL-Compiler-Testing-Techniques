
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size):
        v1 = torch.cat([x1, x1], dim=1)
        v2 = v1[:, :size]
        v3 = torch.cat([v1, v2], dim=1)
        return v3
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2, 64, 64)
size = x1.shape[2] * x1.shape[3]

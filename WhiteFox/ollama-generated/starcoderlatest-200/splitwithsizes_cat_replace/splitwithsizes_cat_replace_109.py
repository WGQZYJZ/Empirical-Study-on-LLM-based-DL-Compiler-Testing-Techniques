
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.split(x2, 3, dim=0)
        v1 = v[0] + v[1]
        return v

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 64) # 1 channel image of shape [C x H x W] (where C = 3)
x2 = torch.randn(3, 64, 64) # 3 channels image of shape [C x H x W] (where C = 3)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, 4)
 
    def forward(self, x):
        v0  = self.conv1(x)
        v1 = (v0 > 0).float() * negative_slope 
        return torch.where(v1 == True, v0, v1), v1

# Initializing the model
m = Model()


# Inputs to the model
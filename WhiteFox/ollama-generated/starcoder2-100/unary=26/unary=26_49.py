
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convTranspose(x1)
        v2  = (v1 > 0).float() * (-negative_slope + torch.sqrt((-(v1 ** 2))) + negative_slope)
        v3  = torch.where(v2 != 0, v1, v2)
        return v3


# Initializing the model
m = Model(0.5)



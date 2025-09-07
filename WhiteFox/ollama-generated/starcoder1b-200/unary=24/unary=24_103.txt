
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1e-6):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).type_as(x1)
        v2 = torch.where(mask, v1, negative_slope * v1)
        return v2


# Initializing the model
m = Model()



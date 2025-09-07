
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1] * len([torch.randn_like(v1), v1]), dim=0) # Concatenating along the channel dimension (dimension 1).
        return v2

# Initializing the model
m = Model()


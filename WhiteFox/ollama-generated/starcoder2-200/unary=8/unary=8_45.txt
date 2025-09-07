
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.conv2  = torch.nn.ConvTranspose2d(8, 5, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2  = v1 + 3
        v3  = F.relu6(v2, inplace=False)
        v4  = torch.clamp(v3, min=0)
        v5  = self.conv2(v4)
        v6  = torch.sigmoid(v5) / 6
        return v6
# Initializing the model
m  = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x):
        v0  = self.conv(x) 
        v1  = F.relu(v0, inplace=True)
        return v1

# Initializing the model
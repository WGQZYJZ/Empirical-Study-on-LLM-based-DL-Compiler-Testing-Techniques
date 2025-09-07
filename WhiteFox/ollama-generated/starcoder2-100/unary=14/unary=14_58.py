
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=5)
        self.glu   = nn.Sequential(
            nn.ReLU(), 
            nn.ConvTranspose2d(in_channels=8, out_channels=4, kernel_size=1), 
            nn.Sigmoid()
        )
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2
        return v3


m = Model()

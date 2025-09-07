
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1, padding=0)
        self.convTranspose = torch.nn.ConvTranspose2d(8, 3, kernel_size=4, stride=2, padding=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        v3 = self.convTranspose(v2)
        return v3

# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(1, 8, 64, 64)

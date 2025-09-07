
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu_(v1)
        v3 = v2 * 0.5
        v4 = torch.max_pool2d(v3, kernel_size=7, stride=(1, 1), padding=(0, 0))
        v6 = self.conv(x4)
        return v6

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(8, 32, 507, 507)
__output__  = m(x1)
 

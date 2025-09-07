
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(3, 4, kernel_size=7)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()
 
 # Inputs to the model 
 x1  = torch.randn(8, 3, 456, 700)
 __output__  = m(x1)

# Initializing the model
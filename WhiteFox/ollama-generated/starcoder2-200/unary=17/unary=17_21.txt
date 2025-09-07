
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(8, 3, kernel_size=64)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.relu(v1)
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 8, 64, 32)
__output__  = m(x1)




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1):
        v0 = torch.sigmoid(x1)
        return self.conv1(v0)


# Initializing the model
m  = Model()
 
 # Inputs to the model 
 __output__  = m(torch.randn(1, 8, 64, 64))

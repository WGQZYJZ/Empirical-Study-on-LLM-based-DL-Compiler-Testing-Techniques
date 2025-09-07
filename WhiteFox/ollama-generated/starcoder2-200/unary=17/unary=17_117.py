
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v0  = conv(x1)
        v1  = nn.ReLU()(v0)
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model
 x2 = torch.randn(4, 3, 64, 64)
 __output__  = m(x2)
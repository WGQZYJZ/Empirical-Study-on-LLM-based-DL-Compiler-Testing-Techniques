
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0  = torch.randn(4, 3, 576, 792) # Input to the model. Use any tensor here.
        v1  = self.conv(v0) 
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = m(None)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v0  = self.conv(x1)
        v1  = torch.sigmoid(v0) # <-
        return v1


# Initializing the model
m  = Model()
__output__  = m(x2)
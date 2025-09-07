
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = self.sigmoid(v1)
        return v2

# Initializing the model
m  = Model()
__output__  = m(x1)


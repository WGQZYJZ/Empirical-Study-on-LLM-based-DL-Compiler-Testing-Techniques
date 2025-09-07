
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = self.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(8, 3, 50, 60)

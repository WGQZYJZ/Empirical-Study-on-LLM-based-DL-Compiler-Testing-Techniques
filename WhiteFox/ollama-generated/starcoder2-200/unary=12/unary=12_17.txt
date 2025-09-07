
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v0  = self.conv(x1)
        v4  = self.sigmoid(v0)
        v5  = v0 * v4
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(3, 8, 64, 64)
 __output__  = m(x1)


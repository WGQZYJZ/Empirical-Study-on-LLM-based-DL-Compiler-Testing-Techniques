
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.ConvTranspose1d(4, 8, 2)
 
    def forward(self, x1):
        v1  = self.conv1d(x1)
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m  = Model()
__output__  = m(torch.randn(4))


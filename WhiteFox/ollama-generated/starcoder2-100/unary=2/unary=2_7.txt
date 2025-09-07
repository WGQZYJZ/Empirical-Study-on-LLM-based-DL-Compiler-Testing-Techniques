
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 + torch.tanh(v2 - (torch.rand_like(v1) * 0)) * v2
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
__output__  = m(x1)
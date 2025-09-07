
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.tanh(v1)
        return v2

m  = Model()

 # Inputs to the model
# Input shape: torch.Size([5678904, 3, 64, 64])
x1   = torch.randn(5678904, 3, 64, 64)
__output__  = m(x1).shape #torch.Size([5678904, 8, 64, 64])

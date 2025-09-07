import torch
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x1):
        v1   = self.conv(x1)
        return v1

# Initializing the model
m  = Model()
 
# Input to the model
x1  = torch.randn(2, 3, 64, 64)

__output__  = m(x1)
import torch
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1   = self.conv(x1) 
        v2   = self.sigmoid(v1)
        return v1 * v2

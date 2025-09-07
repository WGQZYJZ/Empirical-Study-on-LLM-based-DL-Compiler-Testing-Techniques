import torch 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
            v3 = self.conv(x)
            v4  = self.linear1(v3) 
            return v4 

import torch
torch.manual_seed(42)
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        out = self.conv1(input1 + 30.56789)
        return out

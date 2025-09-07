
import torch.nn as nn
 
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = nn.MultiheadAttention(128, 64)
 
    def forward(self, input):
        v1  = self.attn(input)[0]
        return v1


m = Model()
 

import torch
from torch import nn
 
class Model(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return x1
 
 
def main():
    # initializing the model 
    m = Model()
    
    # inputs to the model
    x1 = torch.randn(4, 3)
 
    # obtaining the output of the model  
    

import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(16, 16)
        
    def foward(self, x1):
        v1 = self.fc(x1) 
        v2 = v1 - other
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = (torch.randn(1, 16))
value = 9

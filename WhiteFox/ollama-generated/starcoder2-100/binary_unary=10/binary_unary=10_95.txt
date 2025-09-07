
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(128*3 + 5, 96)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        return v1


# Initializing the model and setting the seed for reproducible results. 
import torch
import numpy as np
torch.manual_seed(42345) # The actual model's hidden state will be different from the given seed
m = Model()
x1 = torch.randn(6, 97 + 3)*0.5


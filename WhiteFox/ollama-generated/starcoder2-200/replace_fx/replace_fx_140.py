

import torch
from pytorch_model_repair import graph_match as gm 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1):
        v2 = torch.nn.functional.dropout(x1, p=0.5) # Apply dropout to the input tensor
        v3 = torch.rand_like(v2).type(torch.int64)  # Generate a tensor with the same size as the output of dropout filled with random numbers

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 3, 10, 256)

__output__  = m(x1) # The output of the forward call


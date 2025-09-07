
import torch 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.functional.linear
 
    def forward(self, x1, x2):
        v1  = self.matmul(x1, x2) # Compute the dot product of two tensors.
        return v1
 
# Initializing a model
m = Model() 


import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dot = torch.nn.DotProduct(scaling=1/50.)
 
    def forward(self, x1):
        query  = x1
        key  = query.transpose(-2, -1)
        v_out  = self.dot(query, key) 
        return v_out

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(4, 8, 50)
 
 __output__  = m(x1)
 
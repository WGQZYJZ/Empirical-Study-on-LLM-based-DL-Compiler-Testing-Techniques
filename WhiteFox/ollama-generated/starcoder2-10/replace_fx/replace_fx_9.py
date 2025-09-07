import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = self._myDropout(x1) # The model contains a dropout node
        v2  = self._myRandLike(v1) # The model contains another randlike node 
        return [v1]
    @staticmethod    
    def _myDropout(input_tensor):
        return torch.nn.functional.dropout(input_tensor, 0.5)
    
    @staticmethod  
    def _myRandLike(input_tensor):
         return input_tensor * (2 * torch.rand(*input_tensor.shape) -1)
    
# Initializing the model with a dropout node and another randlike node:
m = Model()

# Inputs to the model
x1  = torch.randn(3,4)
__output__  = m(x1)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v2 = torch.cat([v] * 500 + [torch.tensor(0)], 3) 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
__input1__ = torch.randn(1, 84, 96) # First input tensor
__input2__ = torch.randn(1, 84, 3072) # Second input tensor 

# Output of the model

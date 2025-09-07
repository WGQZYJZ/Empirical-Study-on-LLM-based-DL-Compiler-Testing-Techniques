
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1  = torch.mm(x1, x2) 
        v2  = torch.mm(x3, x4)
        return v1 + v2

# Initializing the model
m = Model()
 
__inputs_shape__  = (800, 96),  # Shape of input tensor
__outputs_shape__ = (),          # Shape of output tensor
__inputs_dtype__   = torch.float32  # Input data type


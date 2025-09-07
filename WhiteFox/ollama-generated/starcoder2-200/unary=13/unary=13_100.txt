
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.zeros_like(x1) # Initialize a 0 tensor the same size as input tensor
        v3 = v2 * sigmoid(v4)
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
__input1__,  __input2__  = torch.randn(1, 80),  torch.randn(1, 3) 

# Predicting the output of the model on the input tensors 
__output_1__ = m(__input1__)

# Predicting the output of the model on the input tensor with different size than __input1__
__output_2__ = m(__input1__,  __input2__)


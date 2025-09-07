
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.zeros((30))
        v3  = linear(x1) # Apply a linear transformation to the input tensor
        v4 = v3 + v2 
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
__input_tensor__ = torch.randn(8, 60)


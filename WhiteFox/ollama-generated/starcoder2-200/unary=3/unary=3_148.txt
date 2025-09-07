
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.zeros((x1)).clone() # We use the original input tensor to initialize a 3d tensor that is of the same size as an input tensor and filled with zeros
        v4  = v2 * 0.5 # We multiply all the values in this zero vector by 0.5. This would be equivalent of applying a pointwise convolution operation with kernel_size=1, followed by multiplication by constant=0.5.
        return v4
 

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

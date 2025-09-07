
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self._convtranspose(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = torch.relu(v1) 
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 30, 58, 67)

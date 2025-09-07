
class Model(torch.nn.Module):
    def __init__(self, input1=None, input2=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8, 1)
 
    def forward(self, x): 
        v1 = self.conv(x) # Apply a pointwise convolution to the input tensor.
        v2 = torch.mm(input1, input2) # Perform matrix multiplication on two input tensors.
        v3 = torch.cat([v1, v1], dim=0)  # Concatenate along the specified dimension of size 0 in the case of a two-dimensional tensor.
        return v3


# Initializing the model
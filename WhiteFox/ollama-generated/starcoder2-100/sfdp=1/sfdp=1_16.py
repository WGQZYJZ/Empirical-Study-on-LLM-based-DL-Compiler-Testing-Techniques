
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.matmul(x1, query) # Apply pointwise convolution with kernel size 3 to the input tensor
        return v2


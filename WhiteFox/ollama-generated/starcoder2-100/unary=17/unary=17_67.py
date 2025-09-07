
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = torch.nn.functional.relu(v1)  # Apply ReLU activation function to output of conv_transpose with bias=False
        return v2

# Initializing model
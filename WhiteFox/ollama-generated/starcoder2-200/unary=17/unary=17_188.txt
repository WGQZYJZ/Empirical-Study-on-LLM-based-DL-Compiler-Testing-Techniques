
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.conv_transpose2d(x1)  # Apply pointwise transposed convolution to the input tensor
        v2 = nn.functional.relu(v1)     # Apply the ReLU activation function to the output of the transposed convolution
        return v2


# Initializing the model and generating inputs
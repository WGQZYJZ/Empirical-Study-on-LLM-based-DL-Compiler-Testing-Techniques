
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = self.convT(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = torch.relu(v1) # Apply ReLU activation function to the output of the transposed convolution 
        return v2

# Initializing the model
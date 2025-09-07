
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = self.conv2dtranspose(x)  # Apply a pointwise transposed convolution to an input tensor, call the result t4 
        v5 = torch.nn.functional.relu(t3)  # Apply the ReLU activation function to the output of the transposed convolution, call the result t6
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(200, 48, 7, 3) # Input shape is 200 samples of 48 channels with size [7 x 3]
__output__  = m(x1)


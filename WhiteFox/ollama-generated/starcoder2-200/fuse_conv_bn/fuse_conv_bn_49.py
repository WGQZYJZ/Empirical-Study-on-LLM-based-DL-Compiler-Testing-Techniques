
class ConvBN(torch.nn.Module):
    def __init__(self, input_channels):
        super().__init__()

        self.conv = torch.nn.Conv2d(input_channels, 10, kernel_size=3) 
        # This layer is initialized with random weights and biases. 
        self.batchnorm = torch.nn.BatchNorm2d(num_features=10)
        # This layer is initialized with random weights but its running mean, standard deviation (for tracking batch statistics), and momentum parameters are set to 0.

    def forward(self, input): 
        v1 = self.conv(input) # Apply the convolution function on an input tensor.
        return torch.nn.functional.batchnorm(v1, v2)

m = ConvBN(3)
x = torch.randn(5, 3, 28, 28) 

# Inputs to model

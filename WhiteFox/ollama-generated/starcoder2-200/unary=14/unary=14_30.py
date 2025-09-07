
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(64, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv1(x1) # Apply a transposed convolution to the input tensor
        v2 = nn.Sigmoid()(v1) # Apply the sigmoid function to the output of the transposed convolution
        v3 = v1 * v2 # Multiply the output of the transposed convolution by the output of the sigmoid function
        return v3


# Initializing the model
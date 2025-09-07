
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1x1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2x2 = torch.nn.ConvTranspose2d(in_channels=8, out_channels=4, kernel_size=(2, 2), stride=(2, 2))
 
    def forward(self, x1):
        v1  = self.conv1x1(x1) # Apply a pointwise convolution with a 3×3 kernel size to the input tensor
        v2  = torch.sigmoid(v1)# Apply the sigmoid function to the output of the transposed convolution
        v3  = torch.mul(self.conv2x2(v2), v1) # Multiply the output of the transposed convolution by the output of the sigmoid function
        return v3

# Initializing the model
m = Model()


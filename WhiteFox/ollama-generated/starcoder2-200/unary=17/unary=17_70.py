
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = F.relu(x1)  # Apply the ReLU activation function to the input tensor
        v1  = self.conv(v0)  # Apply a pointwise transposed convolution to the input tensor
        return v1


# Initializing model2 with different values from model
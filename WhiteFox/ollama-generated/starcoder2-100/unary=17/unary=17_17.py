
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, kernel_size=5)

    def forward(self, x1):
         v1  = self.conv1(x1) # Apply pointwise transposed convolution to the input tensor
         v2  = F.relu(v1) # Apply the ReLU activation function to the output of the transposed convolution
         return v2

# Initializing the model
m  = Model()


# Inputs to the model
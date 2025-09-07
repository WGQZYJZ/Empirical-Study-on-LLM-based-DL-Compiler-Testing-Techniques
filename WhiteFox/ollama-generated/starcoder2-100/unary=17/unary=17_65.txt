
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x):
        v1  = self.convTranspose(x) # Apply a pointwise transposed convolution to the input tensor
        v2 = F.relu(v1) # Apply ReLU activation function to the output of the pointwise transposed convolution
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(8, 3, 4096 , 4096)

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)

    def forward(self, x):
        v1 = self.conv(x) # Apply pointwise transposed convolution to the input tensor
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the transposed convolution
        return v2


m  = Model()

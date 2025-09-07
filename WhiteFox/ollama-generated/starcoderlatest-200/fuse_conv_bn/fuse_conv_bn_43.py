
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=1, out_channels=24, kernel_size=5)  # Input: [B, C, H, W] Output: [B, 64, 7, 7]
        self.batch_norm1 = torch.nn.BatchNorm2d(24)

    def forward(self, x):
        v1 = torch.nn.functional.conv2d(x, self.conv1.weight, self.conv1.bias, self.conv1.stride, self.conv1.padding) # Apply the convolution function to the input
        v2 = self.batch_norm1(v1)  # Apply the batch normalization function to the output of the convolution layer
        return v2


# Initializing the model
m = Model()
x = torch.randn(1, 3, 7, 7)

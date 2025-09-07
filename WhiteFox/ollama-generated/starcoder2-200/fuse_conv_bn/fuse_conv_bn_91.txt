
class ConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(1, 32, kernel_size=7) # Convolution layer with 32 output channels, using a 7x7 kernel size
        self.bn  = torch.nn.BatchNorm2d(num_features=32)    # Batch normalization layer with 32 input features

    def forward(self, x):
        v1 = torch.nn.functional.relu(self.conv(x))          # Apply ReLU to the convolution output
        return self.bn(v1)

# Initializing and running the model:
model  = ConvBnModel()
output  = model(torch.randn(1, 32, 56, 56))


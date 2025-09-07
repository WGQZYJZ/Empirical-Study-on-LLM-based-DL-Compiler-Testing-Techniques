
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()

        # This conv will be fused into 3x3 convolution
        self.conv1 = nn.Conv2d(in_channels=8, out_channels=8, kernel_size=(5, 7),
                               padding=[0, 1], stride=1)
        # This batch norm is not fusable with 3x3 conv above (no tracking)
        self.bn2 = nn.BatchNorm2d(num_features=8)
        # This conv and batch norm are fused together in eval mode 
        self.conv3 = nn.Conv2d(in_channels=16, out_channels=9, kernel_size=(5, 7),
                               padding=[0, 0], stride=1)

    def forward(self, x):
        x = self.bn2(x)

## Input: batch of 3 images (width and height 8 each with 8 channels each)
input_tensor = torch.randn(batch_size, in_channels, width, height)

 # Initialize the model
m = MyModel()

 # Generate outputs for this model
__outputs__ = m(input_tensor)
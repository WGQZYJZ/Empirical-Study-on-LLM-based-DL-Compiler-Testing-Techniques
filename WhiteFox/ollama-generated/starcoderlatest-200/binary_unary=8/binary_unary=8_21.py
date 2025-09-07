
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # Add another tensor to the output of the convolution
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
other = torch.randn(1, 8, 64, 64) # Shape: (batch_size, output_channels, height, width). Batch size is arbitrary. For simplicity we generate this tensor in the forward function.
x1 = torch.randn(1, 3, 64, 64)

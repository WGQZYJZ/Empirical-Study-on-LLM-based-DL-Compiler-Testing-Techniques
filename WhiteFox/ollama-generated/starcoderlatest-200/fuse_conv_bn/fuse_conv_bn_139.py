
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.functional.conv2d(...)  # Conv2d layer in functional api
        bn = torch.nn.BatchNormXd(..., track_running_stats=False) # BatchNorm layer with running statistics disabled
        output = bn(conv(x1)) # Apply batch norm after the convolution
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2, 2)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
        self.pool = torch.nn.MaxPool2d((1, 2))
 
    def forward(self, x):
        v1 = self.conv1(x)  # Compute the convolution over all input channels for the first timestep
        v2 = self.conv2(v1)  # Compute the convolution over channel 0 of the output from conv1
        v3 = self.pool(v2)  # Max-pool over channel 1 to produce a single feature map (no strides). We use (1, 2) as the window size.
        return v3


# Initializing the model
m = Model()


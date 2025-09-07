
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1) # Conv layer with kernel size (1, 1), stride = 1 and padding = (0, 0)
        self.conv2 = torch.nn.Conv2d(8, 16, 1) # Conv layer with kernel size (1, 1), stride = 1 and padding = (0, 0)
 
    def forward(self, x):
        v1 = self.conv1(x)  # Conv layer 1 with kernel_size (1, 1), stride = 1 and padding = (0, 0)
        v2 = torch.relu(v1)    # Relu activation
        v3 = self.conv2(v2)  # Conv layer 2 with kernel_size (1, 1), stride = 1 and padding = (0, 0)
 
        # Concatenate the two feature maps from conv layers to form a single feature map in the output tensor.
        
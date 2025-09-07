
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...) # X should match with ConvXd

    def forward(self, input_tensor):
        conv = self.conv(input_tensor) # Fuse the two layers to form a single layer
        bn   = self.bn(conv)       # Remove the batch norm layer from the model
        output = bn(input_tensor)  # Perform actual computation on the fused convolution

        return output


# Initializing the model
m = Model()


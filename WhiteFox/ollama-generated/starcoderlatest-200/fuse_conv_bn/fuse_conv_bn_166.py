
class Conv1d(torch.nn.Module):
    def __init__(self, kernel_size):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)
        # Batch normalization layer is used with a different group size than conv layer: 
        # The first layer does not have the batchnorm layer
        self.bn = torch.nn.BatchNorm2d(kernel_size=kernel_size * 2, num_features=kernel_size)
        self.linear = torch.nn.Linear(...)

    def forward(self, x):
        # The original conv layer is not fused to the batch norm layer:
        output1 = self.conv(x)
        # The first layer does not have batchnorm layer as well:
        output2 = self.bn(x) 
        
        return self.linear(output2)


# Initializing the model
c = Conv1d(3)

# Inputs to the model
x1 = torch.randn(1, 4, 6)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)
        self.bn1  = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        conv_out = self.conv1(x) # Apply convolution layer
        output    = self.bn1(conv_out)  # Batch normalization is executed after convolution layer has been applied 
        return output

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 2, 3, 4)

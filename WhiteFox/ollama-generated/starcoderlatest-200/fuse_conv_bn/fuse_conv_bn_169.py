
class ConvBNModel(torch.nn.Module):
    def __init__(self, C, H=32, W=32):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(C, 64, kernel_size=(5, 5))
        self.bn1 = torch.nn.BatchNorm2d(64)

    def forward(self, x):
        x = self.conv1(x) # Conv layer with the output of BN layer before input
        x = F.relu(x) # Non-linearity (ReLU)

        x_bn = self.bn1(x) # Batch norm layer followed by ReLU

        return x

# Initializing the model
model = ConvBNModel(3, H=28, W=28)


# Inputs to the model
x  = torch.randn(1, 3, H=28, W=28)

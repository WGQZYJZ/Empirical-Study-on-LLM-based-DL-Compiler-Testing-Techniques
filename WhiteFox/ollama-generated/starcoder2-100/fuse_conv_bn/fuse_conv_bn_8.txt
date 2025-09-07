
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=7) # Conv with kernel size of 7
        self.bn1 = torch.nn.BatchNorm2d(64)

    def forward(self, x):
        # Forward pass: Conv with BN
        x = x + 5
        y  = torch.nn.functional.conv2d(x, self.conv1.weight)
        y = self.bn1(y)
        return y


# Initializing the model
m  = Model()

# Input to the model
__input__  = torch.randn(3, 3, 4096 , 4096)
__output__  = m(__input__)

The resulting output of the input tensor is stored under __output__.
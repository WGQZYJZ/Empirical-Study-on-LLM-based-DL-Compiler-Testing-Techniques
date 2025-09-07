
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.pool = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
    
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.pool(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(10, 3, 64, 64)

# Calling the model's forward function and returning its outputs
outputs = m(x)


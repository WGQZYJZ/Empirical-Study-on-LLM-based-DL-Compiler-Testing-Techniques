
class Model(torch.nn.Module):
    def __init__(self, kernel_size):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, 48, kernel_size)

    def forward(self, x):
        conv = torch.nn.functional.relu(torch.nn.functional.conv2d(x, self.conv1.weight))
        
        return conv

# Initializing the model
m = Model((7,5,))


# Inputs to the model
x  = torch.randn(480 ,3)
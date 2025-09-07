
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)  # Note: The kernel size in this case is 1 for two reasons. Firstly, we have only one convolutional layer and secondly, we already know the shape of inputs.
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
    
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()



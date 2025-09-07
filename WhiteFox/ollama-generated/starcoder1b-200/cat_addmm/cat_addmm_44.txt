
class Model(torch.nn.Module):
    def __init__(self, width, depth):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(width, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=1)
 
    def forward(self, x):
        # ...
        t = self.conv2(torch.cat([v], dim))  # Concatenate the result along a specified dimension
        # ...
        return t


# Initializing the model
m = Model(4, 8)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        return v1  # Concatenate the result along a specified dimension


# Initializing the model
m = Model()

# Inputs to the model
t1 = torch.randn(1, 3, 64, 64)

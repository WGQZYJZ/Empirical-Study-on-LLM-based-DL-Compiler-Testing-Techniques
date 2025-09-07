
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        # Concatenate along the first dimension
        v1 = self.conv1(x).flatten(start_dim=1)
        v2 = torch.cat([v1, v1, ..., v1], dim=1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(4, 5, 64, 64)

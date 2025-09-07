
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 5, stride=1, padding=2)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.cat([v1, v2], dim=0)  # Concatenate two tensors along a specified dimension
        return v3


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        # Concatenation of the result tensor along a specified dimension
        return torch.cat([v1, v1, ...]


# Initializing the model
m  = Model()



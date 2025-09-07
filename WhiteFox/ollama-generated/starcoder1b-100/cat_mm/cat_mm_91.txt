
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = torch.cat([v1, v1, ..., v1], 1) # Concatenation of the result tensor along the first dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(1, 3, 64, 64)
input2 = torch.randn(1, 8, 64, 64)

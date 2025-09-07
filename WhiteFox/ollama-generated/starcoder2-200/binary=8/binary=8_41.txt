
class Model(torch.nn.Module):
    def __init__(self, input1=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 1 # This line is not in the pattern

# Initializing the model
m = Model()


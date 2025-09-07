
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, size):
        v1 = torch.cat((x1[:, :size], x1), dim=1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 64, 64)
size = 9223372036854775807 # max value of type long

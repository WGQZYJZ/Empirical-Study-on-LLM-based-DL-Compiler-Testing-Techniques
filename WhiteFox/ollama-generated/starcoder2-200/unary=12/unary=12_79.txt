
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2 # <-- add a space here
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
__inputs__  = x1

# Outputs of the model
__outputs__ = m(x1)
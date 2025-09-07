
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 - other
        v4  = torch.nn.ReLU()(v2)
        return v4

# Initializing the model
m = Model()


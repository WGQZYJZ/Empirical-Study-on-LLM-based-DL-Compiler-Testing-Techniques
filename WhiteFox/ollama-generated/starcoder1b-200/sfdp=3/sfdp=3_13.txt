
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(3, 8, 64, 64)
key    = torch.randn(8, 16, 64, 64)
value  = torch.randn(8, 16, 64, 64)
__output__  = m(query, key, value)


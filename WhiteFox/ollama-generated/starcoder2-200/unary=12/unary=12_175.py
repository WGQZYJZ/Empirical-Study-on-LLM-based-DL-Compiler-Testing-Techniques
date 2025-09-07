
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Initializing the optimizer with learning rate 0.01 and momentum 0.9
optimizer = torch.optim.SGD(m.parameters(), lr=0.01, momentum=0.9)


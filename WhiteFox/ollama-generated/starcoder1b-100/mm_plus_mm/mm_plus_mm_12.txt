
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=2)
        self.conv2 = torch.nn.Conv2d(8, 8, 5)

    def forward(self, x1, x2):
        # Add two separate matrix multiplications and concatenate them together
        m = self.conv1(x1) * self.conv2(x2) + torch.mm(x2, x1)
        return m


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 4, 8)
x2 = torch.randn(4, 5, 6, 7)


class ResNet_A(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 32)
        self.layer1 = nn.MaxPool2d((2, 2), stride=2)
        self.linear2 = torch.nn.Linear(32, 16)

    def forward(self, x):
        # Residual units on input of a convolutional layer: t_i = conv(t_(i-1)) * s + i*(conv(t_(i-1)))
        t1 = self.linear1(x)
        s = self.layer1(x)  # Get input (28, 28)
        t3 = t1 * s + __output__
        return t3


# Initializing the model
m = ResNet_A()



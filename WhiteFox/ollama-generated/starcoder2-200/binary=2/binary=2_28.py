
class Model(torch.nn.Module):
    def __init__(self, other=0.3):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - self.other
        return v2


# Initializing the model with the input tensor 0.3 for the scalar 'other' parameter of the model
m = Model()


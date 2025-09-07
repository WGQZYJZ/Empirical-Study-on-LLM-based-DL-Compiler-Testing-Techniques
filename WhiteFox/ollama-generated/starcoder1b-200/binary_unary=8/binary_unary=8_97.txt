
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, other):
        v1 = self.conv(x1) + other  # The output of the convolution is added to a constant 'other' and then ReLU function applied
        return torch.relu(v1)


# Initializing the model
m = Model()


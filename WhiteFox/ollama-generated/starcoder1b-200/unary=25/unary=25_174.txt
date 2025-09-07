
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8, 4)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * -1  # The negative slope is the same as that of Leaky ReLU activation function, so it's just a trick to create the linear transformation as before
        v4 = torch.where(v2, x1, v3)
        return v4


# Initializing the model
m = Model()



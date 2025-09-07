
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)

    def forward(self, x1, x2):
        x1_t = self.conv1(x1)
        x2_t = self.conv2(x2)
        return x1_t * x2_t


# Initializing the model
m = Model()
__input__  = torch.randn(1, 3, 64, 64)  # Input tensor for the first conv layer of the model

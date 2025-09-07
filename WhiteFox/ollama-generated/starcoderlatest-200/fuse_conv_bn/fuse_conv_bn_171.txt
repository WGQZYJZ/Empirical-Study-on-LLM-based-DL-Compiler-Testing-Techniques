
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 3)

    def forward(self, x1):
        output = F.batch_norm(...)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1, 4, 4)


class Model(torch.nn.Module):
    def __init__(self, negative_slope = 10e-3) -> None:
        super().__init__()
        self.convtrans = torch.nn.ConvTranspose2d(8, 3, kernel_size=kernel_size, stride=stride)

    def forward(self, x):
        v1 = self.convtrans(x)
        v2 = v1 > 0

        return torch.where(v2, v1, -negative_slope * v1)


# Initializing the model
m = Model()


# Inputs to the model
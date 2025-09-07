
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3471):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(
            8, 3, kernel_size=(1, 1), stride=1, padding=(0, 0)
        )

    def forward(self, x):
        v1 = self.convT(x)
        v2 = (v1 > 0).float() * (-negative_slope)
        return torch.where(
            v2 < -589, v1 + (-589), v2 + v1 / negative_slope
        )


# Initializing the model
negative_slope= 0.3471 # Initialize a value for negative slope
m = Model(negative_slope)


# Inputs to the model
x = torch.randn(
    1, 8, 64, 64,
)

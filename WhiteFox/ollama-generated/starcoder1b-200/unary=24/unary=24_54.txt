
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1) > 0  # Boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2 = -0.5 * v1  # Negative slope multiplier
        v3 = torch.where(v1, x1, v2 * x1)  # Select elements from t1 or t2 based on boolean mask
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

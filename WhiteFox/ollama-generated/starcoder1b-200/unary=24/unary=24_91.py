
class Model(nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = F.leaky_relu(self.conv(x1), negative_slope)
        v2 = x1 * (-0.7071067811865475 + negative_slope)
        v3 = torch.where(t2, x1, v2)  # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v3


# Initializing the model
m = Model()



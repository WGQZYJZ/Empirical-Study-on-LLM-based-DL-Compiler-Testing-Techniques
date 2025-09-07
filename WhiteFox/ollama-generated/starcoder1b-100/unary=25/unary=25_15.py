
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 >= 0).type(torch.Tensor) * v1 # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        v3 = -2. * self.conv.weight / (self.conv.weight ** 2).sqrt() * x1 + (torch.abs(v2) < 1).float().type(torch.Tensor) # Apply a LeakyReLU to both t1 and t3

        return torch.where(t2, v1, v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

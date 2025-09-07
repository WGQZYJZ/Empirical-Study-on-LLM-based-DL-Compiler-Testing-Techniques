
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1.0e-2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1, negative_slope * v1) # Multiply the output of the convolution by a negative slope based on t1 > 0
        return v2


# Initializing the model
m = Model()
negative_slope = 1.0e-2



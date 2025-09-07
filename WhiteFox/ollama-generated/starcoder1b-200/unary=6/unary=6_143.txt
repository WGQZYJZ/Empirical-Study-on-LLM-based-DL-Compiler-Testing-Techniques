
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = v1.clamp_(min=0)  # Clamp the output of the addition operation to a minimum of 0
        v3 = v2.clamp_(max=6)  # Clamp the output of the previous operation to a maximum of 6
        v4 = v1 * v3  # Multiply the output of the convolution by the output of the clamp operation
        v5 = v4 / 6  # Divide the output of the multiplication operation by 6
        return v5


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1, x2)
        v2 = v1 + v1  # The results of the matrix multiplications are added together
        return v2


# Initializing the model
m = Model()


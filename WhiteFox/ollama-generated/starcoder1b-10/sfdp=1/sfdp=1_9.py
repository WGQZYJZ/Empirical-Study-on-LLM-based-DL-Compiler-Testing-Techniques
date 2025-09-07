
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
 
    def forward(self, x1):
        x1_out = self.conv1(x1)
        x2_out = self.conv2(x1_out)
        return x2_out


# Initializing the model
m = Model()



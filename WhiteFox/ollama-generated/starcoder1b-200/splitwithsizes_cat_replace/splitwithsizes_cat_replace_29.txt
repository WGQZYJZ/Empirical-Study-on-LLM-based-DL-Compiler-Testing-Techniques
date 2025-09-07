
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [3, 4]
        concatenated_tensor = torch.cat([torch.split(x1, sizes=[3], dim=0), torch.split(x1, sizes=[4], dim=0)], dim=0)
        v = self.conv(concatenated_tensor)
        return True


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

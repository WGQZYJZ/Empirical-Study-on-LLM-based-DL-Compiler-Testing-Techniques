
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1, v1], dim=1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensors = [torch.randn(100, 8, 13, 13), torch.randn(100, 4, 9, 9)]


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        return v1 * v2

 # Initializing the model
m = Model()

 # Inputs to the model
input1  = torch.randn(8, 3, 64, 64)
input2  = torch.randn(8, 3, 64, 64)

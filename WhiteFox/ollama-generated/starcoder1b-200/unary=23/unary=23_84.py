
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(8, 3, 1, stride=1)
 
    def forward(self, x2):
        v2 = self.conv(x2)
        v3 = torch.tanh(v2)
        return v3


# Initializing the model
m = Model()


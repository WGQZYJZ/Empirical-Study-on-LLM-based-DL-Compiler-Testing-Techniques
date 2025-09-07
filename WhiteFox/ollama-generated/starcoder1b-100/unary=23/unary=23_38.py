
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(10, 2, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.tanh(v1)


# Initializing the model
m = Model()



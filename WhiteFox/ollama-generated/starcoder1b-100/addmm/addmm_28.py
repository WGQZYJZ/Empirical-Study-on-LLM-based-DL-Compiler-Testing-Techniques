
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v2 = self.conv(x1) * inp
        return v2


# Initializing the model
m = Model()


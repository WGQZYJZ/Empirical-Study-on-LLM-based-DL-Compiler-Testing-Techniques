
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        if x2 == None:
            inp = torch.randn(x1.shape[0], 8)
        else:
            inp = x2
        v1 = self.conv(x1) * inp
        return v1


# Initializing the model
m = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = self.conv_transpose(x1)
        t2 = torch.sigmoid(t1)
        return t2


# Initializing the model
m = Model()



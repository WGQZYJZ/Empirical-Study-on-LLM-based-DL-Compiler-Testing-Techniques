
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        return self.conv(x2).mm(x1.unsqueeze(0))


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self, x):
        super().__init__()
        self.x = torch.split(x, 2, dim=3)
 
    def forward(self):
        v1 = torch.cat([self.x[i] for i in range(len(self.x))], dim=3)
        return v1


# Initializing the model
m = Model(torch.randn(1, 2, 64, 64))


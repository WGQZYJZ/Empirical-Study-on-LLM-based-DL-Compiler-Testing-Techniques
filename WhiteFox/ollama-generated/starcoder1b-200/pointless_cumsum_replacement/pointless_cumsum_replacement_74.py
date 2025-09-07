
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.full([8, 3], 0)
 
    def forward(self, x1, x2):
        v1 = self.full.view(1, 1, 8, 3).expand(x1.shape)
        return (v1 + x2).add_(1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 4, 50, 50)
x2 = m.full

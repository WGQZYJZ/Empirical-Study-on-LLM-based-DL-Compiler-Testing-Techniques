
class Model(torch.nn.Module):
    def __init__(self, d=None):
        super().__init__()
        self.d = d
 
    def forward(self, x1, x2):
        return torch.cat([x1, x1, x1, x2], dim=self.d)


# Initializing the model
m = Model()



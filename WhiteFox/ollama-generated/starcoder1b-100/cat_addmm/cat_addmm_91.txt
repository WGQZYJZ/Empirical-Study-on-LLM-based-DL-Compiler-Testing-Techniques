
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input = torch.randn(1, 2, 3)
 
    def forward(self, x1, x2):
        v1 = self.input + x1
        return torch.cat([v1, x2], dim=0)


# Initializing the model
m = Model()



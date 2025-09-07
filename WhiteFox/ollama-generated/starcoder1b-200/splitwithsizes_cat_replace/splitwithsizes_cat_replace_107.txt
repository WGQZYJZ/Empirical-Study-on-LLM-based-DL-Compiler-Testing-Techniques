
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4, x5, x6):
        y = torch.cat([x1, x2, x3, x4, x5, x6], dim=1)
        return True


# Initializing the model
m = Model()



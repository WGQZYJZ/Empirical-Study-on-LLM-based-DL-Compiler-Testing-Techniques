
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        return torch.cat([x1, x2, x1, 
                          torch.cat([x2, x2, x2], dim=0)], dim=1)


# Initializing the model
m = Model()



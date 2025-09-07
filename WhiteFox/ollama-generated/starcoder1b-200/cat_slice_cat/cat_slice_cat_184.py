
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x_1, x_2):
        v = torch.cat([x_1, x_2], dim=1)
        return v

# Initializing the model
m = Model()



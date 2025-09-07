
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x1 = self.linear(x1)
        return x1.permute(0, 2, 1)

# Initializing the model
m = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 10)
        v2 = v1.permute(0, -1, 1)
        return v2

# Initializing the model
m = Model()


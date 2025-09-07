
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1, ...)
        return v.permute(...)


# Initializing the model
m = Model()



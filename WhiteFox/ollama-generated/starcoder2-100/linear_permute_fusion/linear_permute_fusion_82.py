
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1, 0)
        return v.permute(2, 1)


# Initializing the model
m  = Model()


# Inputs to the model

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = x1.permute(0, 2, 1)
        # ... use the linear function with v as an input and other parameters in this model
        return t2


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full  = torch.nn.functional.full([arg1, arg2], scalar_value=scalar_value)

    def forward(self, x1):
        v1 = self.full(x1)
        v2 = torch.cumsum(v1, 1)
        return v2


# Initializing the model
m = Model()


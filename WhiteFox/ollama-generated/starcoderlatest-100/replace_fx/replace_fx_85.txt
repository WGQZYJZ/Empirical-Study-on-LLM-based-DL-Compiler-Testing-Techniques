
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        v1 = torch.nn.functional.avg_pool2d(x1)
        v2 = torch.nn.functional.adaptive_max_pool2d(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 5, 5)

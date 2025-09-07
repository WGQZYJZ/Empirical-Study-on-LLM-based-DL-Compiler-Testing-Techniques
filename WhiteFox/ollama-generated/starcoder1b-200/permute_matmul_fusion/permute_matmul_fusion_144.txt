
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.Bmm2d

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = self.bmm(v1, x2)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 4, 2)  # The input tensor shape is 1, 3, 4, 2
x2 = torch.randn(1, 4, 2, 2)  # The input tensor shape is 1, 4, 2, 2

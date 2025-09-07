
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3  = torch.nn.functional.conv2d(x1, self.linear)
        return v3


# Initializing the model
m  = Model()
__output__  = m(x1)


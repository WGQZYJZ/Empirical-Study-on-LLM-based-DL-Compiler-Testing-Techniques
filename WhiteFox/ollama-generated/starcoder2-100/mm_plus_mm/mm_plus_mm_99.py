
class Model(torch.nn.Module):
    def __init__(self, *args):
        super().__init__()
        self.conv = torch.nn.Conv2d(*args)

    def forward(self, x1):  # Matrix multiplication between input1 and input2
        v1 = torch.mm(x1, v1)
        return v1


m = Model()




class Model(torch.nn.Module):
    def __init__(self, length=10):
        super().__init__()

    def forward(self, x):

        return torch.mm(x[i], x[j])


m = Model()  # Generate model instance with the given `length` parameter.

x_list = [torch.randn(32, 64)] * m.length

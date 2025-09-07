
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, dim=None):
        assert isinstance(x1, torch.Tensor)
        assert isinstance(x2, torch.Tensor)
        assert isinstance(dim, int)

        if dim is None:
            return self.__class__.__new__(self).forward(torch.cat([x1, x2], 1), None)
        else:
            return self.__class__.__new__(self).forward(torch.cat([x1[:, 0:9223372036854775807], x2], 1), dim)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 9223372036854775807, 2)

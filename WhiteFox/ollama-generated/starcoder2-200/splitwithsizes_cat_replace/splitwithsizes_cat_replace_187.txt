
class Model(torch.nn.Module):
    def __init__(self, dim=-1, split_sizes=[32], size=64):
        super().__init__()

        self.split = torch.nn.MaxPool2d(size, 8, stride=(0), ceil_mode=True)

    def forward(self, x):
        x_split = torch.split(x, split_sizes, dim=-1)
        return torch.cat([x for x in reversed(x_split)], dim=dim)

# Initializing the model with the default values for the `split` argument.
m = Model()


# Inputs to the model with the default values for the `split` argument:
x1  = torch.randn(size=[8,320 ,64])


# Initializing the model without the `split` argument or the `dim=-1` parameter in the forward method of the model class.
m_not_found  = Model()



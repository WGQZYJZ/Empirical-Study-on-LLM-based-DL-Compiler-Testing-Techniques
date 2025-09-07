
class Model(torch.nn.Module):
    def __init__(self, dim=1, input_tensor=None):
        super().__init__()
        if not input_tensor:
            input_tensor = torch.randn(5, 8)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        split_sizes = (2,) * len(x.shape)

        return is_valid_splitwithsizes_cat((self.conv(x), self.conv(x)), split_sizes)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)

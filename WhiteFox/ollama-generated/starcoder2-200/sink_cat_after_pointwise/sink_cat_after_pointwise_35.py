
class Model(torch.nn.Module):
    def __init__(self, dim1=3072, dim2=4096):
        super().__init__()

        self._conv = torch.nn.Conv2d(in_channels=3, out_channels=dim1, kernel_size=(5, 5), stride=2)

        self._linear = torch.nn.Linear(in_features=dim1 * (784 // dim1 ** 2 - 4), out_features=dim2)

    def forward(self, x):
        v0 = self._conv(x)
        v1 = torch.relu(v0)

        # This will be sunk into the model. Please add a new input.
        t0 = torch.cat((
            [
                v1[:, 0], 
                ...
            ], dim=1), 
        dim=1).contiguous()

        t2 = self._linear(t0)
        return t2



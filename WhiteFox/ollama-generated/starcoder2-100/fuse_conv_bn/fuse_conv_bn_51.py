
class Model(torch.nn.Module):
    def __init__(self, conv: torch.nn.ConvXd, bn: torch.nn.BatchNormNd):
        super().__init__()
        self._conv = conv # ConvXd
        self._bn = bn # BatchNormNd

    def forward(self, input_tensor):
        v1  = self._conv(input)  # ConvXd
        v2  = torch.nn.functional.batch_norm(v1, None, None, 0., 1e-5, True)  # BatchNormXd
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 4, 5)

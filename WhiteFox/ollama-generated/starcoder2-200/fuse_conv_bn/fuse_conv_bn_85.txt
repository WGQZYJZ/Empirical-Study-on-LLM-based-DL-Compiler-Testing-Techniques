
class Model(torch.nn.Module):
    def __init__(self, conv1d: int = 32,
                 kernel1d: int = (4,),
                 batchnorm1d: bool = True) -> None:
        super().__init__()

        self._conv1d  = torch.nn.Conv1d(
            in_channels=784, out_channels=conv1d,
            kernel_size=(kernel1d))
        self._batchnorm2d = torch.nn.BatchNorm1d(num_features=3)

    def forward(self, input):

        # Model 1
        v1 = self._conv1d(input).relu()
        return v1

# Initializing the model and setting parameters
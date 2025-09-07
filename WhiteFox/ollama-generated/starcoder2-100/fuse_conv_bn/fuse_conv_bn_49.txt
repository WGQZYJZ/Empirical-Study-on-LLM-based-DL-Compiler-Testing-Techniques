
class FuseConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self._conv = torch.nn.Conv1d(3, 64, 3)
        self._batchnorm = torch.nn.BatchNorm1d(num_features=64)
        self._relu = torch.nn.ReLU()

    def forward(self, x):
        output = self._relu(
            self._conv(
                self._batchnorm(
                    x)))

        return output


# Initializing the model 
m = FuseConvBnModel()

# Inputs to the model (same as previous one)
x1  = torch.randn(2,3,480)

 # Input tensor for the fused model: 
 __output__  = m(x1)


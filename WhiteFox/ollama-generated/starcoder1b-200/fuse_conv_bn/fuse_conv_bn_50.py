
class ConvModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv1d(...)
        self.bn = nn.BatchNorm1d(...)

    def forward(self, x):
        return torch.nn.functional.conv1d(
            input=x,  # X can be 1, 2, or 3 representing the dimension
            weight=self.conv.weight,
            bias=self.conv.bias,
        ) + self.bn(input)


# Initializing the model
m = ConvModel()



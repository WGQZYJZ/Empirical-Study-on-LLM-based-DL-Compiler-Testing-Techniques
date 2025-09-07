
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)  # ConvXd in functional API

        self.bn = torch.nn.BatchNorm1d(...)  # BatchNormXd in functional API

    def forward(self, x):
        output = self.conv(x)
        bn_output = F.batch_norm(output)
        return bn_output


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 2, 3, 4, 5)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)  # ConvXd is equivalent to Conv1d

    def forward(self, x):
        output = self.conv(x)
        bn_out  = nn.BatchNorm2d(output.shape[-1]) # BatchNormXd can be replaced with nn.BatchNorm2d
        return bn_out(output)

# Inputs to the model
input_tensor = torch.randn(1, 3, 4, 5)

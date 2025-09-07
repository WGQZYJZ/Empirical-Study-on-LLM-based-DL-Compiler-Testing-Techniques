
class UpsampleModel(torch.nn.Module):
    def __init__(self, n_input: int, n_output: int, stride=2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(n_input, n_output, 3, stride, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.sigmoid(v1)


# Inputs to the model
x1 = torch.randn(1, 8, 4, 5, 2)

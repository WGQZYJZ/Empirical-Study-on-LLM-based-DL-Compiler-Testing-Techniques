
class Model(torch.nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_dim, 16, kernel_size=3)

    def forward(self, x1):
        bn = torch.nn.functional.batch_norm(x1, self.conv.weight)
        output = bn(self.conv(x1))
        return output


# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)

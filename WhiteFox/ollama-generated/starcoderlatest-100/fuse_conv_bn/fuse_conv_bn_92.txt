 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(in_channels=2, out_channels=2, kernel_size=(3, 3))
        bn = torch.nn.BatchNorm2d(num_features=4)

        output = bn(conv(x1))
        return output

# Inputs to the model
x1 = torch.randn(1, 2, 4, 5)

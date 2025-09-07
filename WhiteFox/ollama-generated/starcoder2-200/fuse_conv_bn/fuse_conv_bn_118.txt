
class FusedModel(torch.nn.Module):
    def __init__(self, conv: torch.nn.ConvXd = 2) -> None:
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=8, kernel_size=(3, 4), stride=2, bias=True)

        self.bn0 = torch.nn.BatchNorm2d(num_features=self.conv1.out_channels, momentum=0.95, affine=True)

    def forward(self, x: torch.Tensor):
        conv2 = torch.nn.functional.conv2d(x, self.conv1.weight, bias=None, stride=(1, 3), padding=(-3, -4))

        batchnorm0 = self.bn0(conv2)

        return batchnorm0


# Initializing the model
m  = FusedModel()

 # Inputs to the model
x1  = torch.randn(5, 3, 96, 98)


 
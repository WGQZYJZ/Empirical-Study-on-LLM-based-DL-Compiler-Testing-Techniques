
class FusedConvBnModel(torch.nn.Module):
    def __init__(self, conv1d=False, conv2d=True, conv3d=False):
        super().__init__()
        if conv1d:
            self.conv = torch.nn.Conv1d(in_channels=50, out_channels=47, kernel_size=[7])
        else:
            self.conv = torch.nn.Conv2d(in_channels=39, out_channels=38, kernel_size=(6, 6))

        if conv1d:
            self.bn = torch.nn.BatchNorm1d(47)
        elif conv2d:
            self.bn = torch.nn.BatchNorm2d(kernel_size=[25])
        else:
            self.bn = torch.nn.BatchNorm3d(48, track_running_stats=True)

    def forward(self, input):

        return self.bn(torch.nn.functional.conv1d(input, weight))

# Initializing the model
m  = FusedConvBnModel()


# Input to the model
x1  = torch.randn(384, 50) # Assuming conv1d is set to True and conv2d is set to False in the model initialization call above.


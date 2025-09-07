
class Model(torch.nn.Module):
    def __init__(self, in_channels):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=in_channels, out_channels=3)

    def forward(self, x):
        conv  = torch.nn.functional.conv2d(x, self.conv)
        return conv


# Initializing the model
m = Model(in_channels=16)
m.eval()

# Inputs to the model
__input_tensor__  = torch.randn(400,) # 400-D vector is enough for BN, however, it must be 5d or more.


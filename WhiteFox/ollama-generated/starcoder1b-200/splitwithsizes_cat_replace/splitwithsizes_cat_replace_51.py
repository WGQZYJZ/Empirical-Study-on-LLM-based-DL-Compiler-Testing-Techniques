
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        return True if is_valid_splitwithsizes_cat([torch.split(x1, [64, 64]),
                                             torch.split(x1, [32, 32])],
                                             dim=-1) else False


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 32, 64, 64)  # input shape: (batch_size, channels, in_height, in_width)

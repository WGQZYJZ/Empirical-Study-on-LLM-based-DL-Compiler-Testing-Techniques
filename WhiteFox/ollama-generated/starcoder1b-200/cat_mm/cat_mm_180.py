
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # The shape of `x1` is (N, C, H, W), and the shape of `x2` is (C, H, W).
        # We concatenate `x1`, `x2` along channel dimension.
        # So, the shape of output will be (C, H * W).
        return torch.cat([self.conv(x1), self.conv(x2)], 1)


# Initializing the model
m = Model()


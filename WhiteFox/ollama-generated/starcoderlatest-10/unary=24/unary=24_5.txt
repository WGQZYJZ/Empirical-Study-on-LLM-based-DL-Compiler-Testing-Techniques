
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # The shape of the boolean mask is (N, C, H, W), where N is the number of elements in batch data and C is the channel dimension for each input image
        t1 = torch.le(v1, 0)
        v2 = v1 * self.negative_slope
        v3 = torch.where(t1, v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

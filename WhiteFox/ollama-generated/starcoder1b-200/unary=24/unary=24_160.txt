
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).type(torch.float) * self.negative_slope
        v2 = torch.where(mask, v1, v1 * -1)  # Select the elements from v1 or v2 based on mask
        return v2


# Initializing the model
m = Model()



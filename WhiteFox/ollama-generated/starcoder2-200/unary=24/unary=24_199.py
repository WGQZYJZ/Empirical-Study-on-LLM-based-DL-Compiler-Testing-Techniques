
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).float() * -1  # multiplying by zero is not necessary in the where function because the mask is already a boolean mask and will result in elements that are True being multiplied by -1, and all others being multiplied by 0. Alternatively we can pass in the v2 tensor itself to the where function as well
        v3  = self.negative_slope * (v1 < 0) 
        v4  = torch.where(v2 == False, v1 + 1, v3) # create the boolean mask and add one using torch.where, this is equivalent to multiplying by -1 on every element that is less than zero
        return v4


# Initializing the model

class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        # We store the negative slope in a class attribute so that we can easily access it from other functions in the model.
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1   = self.conv(x1)
        mask  = v1 > 0

        # Multiplying with negative slope
        negative_output  = v1 * (-self.negative_slope)

        # Selecting elements based on the mask
        output    = torch.where(mask, v1, negative_output)
 
        return output

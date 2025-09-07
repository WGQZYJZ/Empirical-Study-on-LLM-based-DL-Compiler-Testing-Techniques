
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float() # Create a float tensor where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        neg_mask = mask * - self.negative_slope # Negative value of the mask
        v2 = mask * (x1 * neg_mask)  # Multiply v1 by neg_mask based on a boolean tensor where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        return v2


# Initializing the model
m = Model()



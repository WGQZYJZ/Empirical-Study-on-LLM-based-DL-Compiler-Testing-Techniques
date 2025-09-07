
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float() # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2 = mask * negative_slope # Multiply the output of the convolution by the negative_slope
        return torch.where(mask, v1, v2)


# Initializing the model
m = Model()



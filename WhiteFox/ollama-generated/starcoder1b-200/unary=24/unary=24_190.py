
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1, -v1 * negative_slope) # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3 = v1 * negative_slope # Multiply the output of the convolution by the negative_slope
        return torch.where(v2 == 0, v3, v2)


# Initializing the model
m = Model()

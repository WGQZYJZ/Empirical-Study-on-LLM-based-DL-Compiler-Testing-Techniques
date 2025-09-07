
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv  = torch.nn.Conv2d(16, 8, 7)
        self.negative_slope  = negative_slope
 
    def forward(self, x):
        v1  = self.conv(x) 
        mask = (v1 > 0).to(torch.float32) # Create a boolean mask where each element is True if the corresponding element in v1 is greater than 0 and False otherwise
        v2 = -v1 * self.negative_slope  # Multiply the output of the convolution by the negative slope
        v3  = torch.where(mask, v1, v2) 
        return v3


# Initializing the model
m  = Model(0.3)

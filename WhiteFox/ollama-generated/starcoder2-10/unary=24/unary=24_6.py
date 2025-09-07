
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.329411765):
        super().__init__()
        self.conv  = torch.nn.Conv2d(8, 8, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Create a boolean mask where each element is True if the corresponding 
        # element in v1 is greater than 0 and False otherwise
        mask  = torch.ge(v1, 0).to(torch.bool)
        # Multiply the output of the convolution by the negative_slope
        negative_value  = -negative_slope * torch.ones_like(mask)
        v3  = negative_value + v1 
        # Apply where function to select elements from v1 or v3 based on the mask
        v4 = torch.where(mask, v1, v3)

        return v4


# Initializing the model
m = Model()



# Inputs to the model
x1  = torch.randn(10, 8, 256, 256)
__output__  = m(x1)

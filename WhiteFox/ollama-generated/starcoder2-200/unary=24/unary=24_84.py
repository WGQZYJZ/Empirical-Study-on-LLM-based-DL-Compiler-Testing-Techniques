
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0 # Creates a boolean mask where each element is True if the corresponding element in t1 is greater than 0 and False otherwise 
        v2 = negative_slope * v1   # Multiplies the output of the convolution by the negative slope
        v3 = torch.where(mask, v1, v2) # Selects elements from t1 or t2 based on mask
        return v3

# Initializing the model
m = Model()


# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64)


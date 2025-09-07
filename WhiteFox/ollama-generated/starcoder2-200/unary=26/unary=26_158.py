
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3) #torch.where(mask, y, z) --> mask: The mask to indicate which elements should be set based on the corresponding element in x and y or z; x: Input tensor that will be selected by mask for each position where it's 1; y: Input tensor that will be selected by mask for each position where it's 0;
        return v4

# Initializing the model
negative_slope = torch.tensor(0.25) # Define the negative slope value (e.g., 0.25).
m1, m2 = Model(negative_slope), Model(torch.tensor(-0.3)) # Initialize two models with different negative slopes.
# Inputs to the first model
x1 = torch.randn(1, 3, 64, 64)
__output1__  = m1(x1)
# Inputs to the second model
x2 = torch.randn(1, 3, 98, 78)
__output2__  = m2(x2)


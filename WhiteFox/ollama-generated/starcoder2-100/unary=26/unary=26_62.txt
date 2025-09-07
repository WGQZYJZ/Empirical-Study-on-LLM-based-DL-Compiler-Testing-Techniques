
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convt = torch.nn.ConvTranspose1d(3, 8, kernel_size=1)

    def forward(self, x):
        v1  = self.convt(x) # Apply pointwise transposed convolution to the input tensor
        v2  = v1 > 0        # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3  = torch.where(v2, v1, -negative_slope)  # Apply the where function to select elements from t1 or negative slope based on the mask
        return v3


# Initializing the model and setting negative slope
negative_slope  = 0.25
m = Model(negative_slope=negative_slope)
__output__   = m(__input__)
 

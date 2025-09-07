
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = nn.functional.clamp_min(v1, -10.) # Clamps each element of the input with a minimum value and returns the result.
        v3  = nn.functional.clamp_max(v2, 5., return_mask=False).to("cpu") # Clamps each element in the input to at most the given maximum value. If return_mask is True, returns a boolean mask of same shape as the input, indicating whether each element was clipped
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(20)

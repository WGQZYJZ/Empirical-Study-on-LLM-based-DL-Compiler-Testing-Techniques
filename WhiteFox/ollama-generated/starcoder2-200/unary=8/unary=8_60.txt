
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x) # Apply a pointwise convolution to the input tensor
        v2 = v1 + 3 # Add 3 to the output of the convolution
        v3 = torch.clamp(v2, min=0) # Clamp the output of the addition operation to a minimum of `0`
        v4 = torch.clamp(v3, max=6) # Clamp the output of the previous clamp operation to a maximum of 6
        v5 = v1 * v4 # Multiply the output of the convolution by the output of the clamp operation
        v6 = v5 / 6 # Divide the output of the multiplication operation by `6`
        return v6


# Initializing model and inputs to the model (The input is used in a forward pass in `inference_input.txt`)

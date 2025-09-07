
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0
        v2 = (v1 * -0.5).masked_fill_(~mask, 1) # Create a new tensor based on the input tensor that has each element where the corresponding value of the convolution is `0` but its corresponding value in the output of the transposed convolution is `negative_slope`.
        v3 = (v1 * negative_slope).masked_fill_(~mask, 0) # Multiply the output of the transposed convolution by the negative slope and where based on the mask
        return v2 * v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

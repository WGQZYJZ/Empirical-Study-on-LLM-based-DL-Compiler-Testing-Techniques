
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.t3   = torch.nn.Tanh()
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 * self.negative_slope).type(torch.float32)  # Create a mask where each element is True if the corresponding element in v1 is greater than `0`
        v3 = v2 * self.t3(v1)  # Multiply the output of the transposed convolution by the negative slope
        return torch.where(v2, x, v3)


# Initializing the model
m = Model()



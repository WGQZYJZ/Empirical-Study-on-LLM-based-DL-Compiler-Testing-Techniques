
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1)

        # Subtracting the output of the convolution by a constant
        # and then by another constant
        v4_constant = 5 + 4j
        v3 = torch.sub(v2, v4_constant)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model (input tensor of the same shape as convolution's output)
x1 = torch.randn(1, 8, 60, 57).half().type(torch.half)

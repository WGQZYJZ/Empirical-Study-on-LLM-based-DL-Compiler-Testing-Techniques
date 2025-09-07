
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)

        # apply sigmoid activation to the convolution output in line with the pattern described by the user above 
        v2 = torch.sigmoid(v1)

        # multiply the output of the convolution by the output of the sigmoid function 
        # note that we are using the output from line 4 as input for this multiplication 
        v3 = v1 * v2
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Obtaining output of the model on the inputs x1 
__output__  = m(x1)


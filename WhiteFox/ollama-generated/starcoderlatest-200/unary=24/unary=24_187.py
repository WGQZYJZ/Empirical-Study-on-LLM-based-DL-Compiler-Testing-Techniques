
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Add code that should create a boolean mask and then multiply the output of the convolution by the negative slope

        return v6


# Initializing the model
m = Model()



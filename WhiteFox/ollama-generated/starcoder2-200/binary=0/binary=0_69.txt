
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1,  other=None):

        # If the "other" tensor is not passed, the default value should be 0.
        if other is None:
            other = torch.zeros_like(x1)
        v1 = self.conv(x1) + other
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model (the second input has a default value, so we don't need it for this sample test case)
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + v3  # Added to the output of the convolution is another tensor (v3) which is not passed as a keyword argument to addition operation.
        return v2


# Initializing the model
m = Model()
 
 

# Inputs to the model, where `v3` is not present in the inputs for forward call.
x1  = torch.randn(1, 3, 64, 64)



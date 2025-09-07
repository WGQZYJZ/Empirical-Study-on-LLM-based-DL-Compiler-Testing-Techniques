
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        return v2 + other  # Add another tensor to the output of the convolution
 
 # Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.rand(2, 4, 28, 28)

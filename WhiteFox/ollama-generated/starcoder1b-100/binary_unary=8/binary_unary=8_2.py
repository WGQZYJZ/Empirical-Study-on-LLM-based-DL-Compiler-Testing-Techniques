
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + torch.randn(10, 50, 64, 64) # Add a tensor to the output of the convolution and generate a random value
        v2 = v1 + other  # Add another tensor to the result
        return v2


# Initializing the model
m = Model()


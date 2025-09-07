
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self.conv(x1)  # Perform convolution on input x1
        return v2


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(4, 3, 64, 64, dtype=torch.float32, device="cpu")

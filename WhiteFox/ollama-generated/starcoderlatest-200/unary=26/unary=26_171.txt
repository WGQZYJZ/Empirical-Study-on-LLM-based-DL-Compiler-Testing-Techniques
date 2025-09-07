
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=2)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        # We do not use Leaky ReLU because its derivative will be equal to t4 * (1 - t4) which is the same as t3 in this example
        v2 = torch.where(v1 > 0, v1, torch.tensor(0.1))
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)

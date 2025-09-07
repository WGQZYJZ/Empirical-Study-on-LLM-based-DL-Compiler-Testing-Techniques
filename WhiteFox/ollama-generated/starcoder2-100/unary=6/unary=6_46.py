

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1) + 3

        clamped_value = F.relu6(v1)
        v2 = torch.div(clamped_value, 6.0)

        return v2

m = Model()

# Input to the model
input_tensor  = torch.randn(4, 3, 5, 7) # A random input tensor with size [4 x 3 x 5 x 7]

# Calling the forward pass of the model
output1 = m(input_tensor)


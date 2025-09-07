
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor # Add another tensor to the output of the convolution
        v3 = torch.relu(v2)
        return v3


# Input to the model
x1  = torch.randn(1, 3, 64, 64)
# Other tensor that is added to the output of the previous layer's conv
other_tensor = torch.zeros_like(v1) + 0.5

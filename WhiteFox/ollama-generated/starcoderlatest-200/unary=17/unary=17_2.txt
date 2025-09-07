
class Model_1(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v7 = self.conv_transpose(x2)
        v8 = torch.relu(v7)
        return v8


# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)

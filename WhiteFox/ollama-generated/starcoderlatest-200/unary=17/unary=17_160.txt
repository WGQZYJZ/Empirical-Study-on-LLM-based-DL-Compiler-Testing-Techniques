
class Model_1(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 2, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.relu(v1)
        return v2

# Initializing the model
m_1 = Model_1()

# Inputs to the model
x1_1 = torch.randn(1, 3, 64, 64)
__output_1__ = m_1(x1_1)


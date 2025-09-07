
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2) + 1
        return v3


# Input tensor for the model
input_tensor = torch.randn(1, 3, 64, 64)
print('Input tensor:')
print(input_tensor)

# Predicted output for the input tensor
output = m(input_tensor)


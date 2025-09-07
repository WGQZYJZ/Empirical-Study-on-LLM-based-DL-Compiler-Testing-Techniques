
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = t2 + v1
        v3 = t3 + v2
        return torch.cat([v1, v3], dim=1)


# Inputs to the model
input_tensor  = x1[:, 0:9223372036854775807]
__output__     = m(input_tensor, input_tensor)


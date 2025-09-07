
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) - torch.tensor([0], requires_grad=True)
        v2 = relu(v1)
        return v2


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
other    = 0.5 * torch.randn(1, 3, 64, 64)

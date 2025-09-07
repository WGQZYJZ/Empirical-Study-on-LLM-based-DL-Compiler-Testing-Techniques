
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.elu(self.conv(x1)) * 0.5
        v2 = v1 ** 2
        v3 = torch.nn.functional.conv2d(v2, torch.tensor(4., requires_grad=True), padding=1)
        v4 = v3 / 4
        v5 = F.elu(torch.tanh(v4)) + 1
        v6 = v1 * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 256, 256)

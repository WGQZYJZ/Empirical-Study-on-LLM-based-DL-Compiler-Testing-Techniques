
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.conv_transpose2d(x1, weight=self.weight, output_padding=(0, 0), stride=2) * 0.5
        v2 = torch.pow(v1, 2)
        v3 = torch.pow(v2, 2)
        v4 = torch.mul(torch.addcmul(v3, v1, 1.00001), v3)
        v5 = torch.exp(v4)
        v6 = torch.tanh(v5)
        return torch.mul(v6, v2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 128, 128)

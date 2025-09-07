
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model<|end_of_code|>
m  = Model()

 # Inputs to the model
input__ = [
    torch.randn(1, 3, 64, 64),
]

# Expected output<|end_of_output|>
__expected__  = m(*input__)

__generated__  = torchdxc.infer(m)


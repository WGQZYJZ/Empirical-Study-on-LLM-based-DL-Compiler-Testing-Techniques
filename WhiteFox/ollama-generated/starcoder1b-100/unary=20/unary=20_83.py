
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=2, padding=0)
 
    def forward(self, x1):
        return self.conv(x1) * 0.7071067811865476


# Inputs to the model
x1 = torch.randn(3, 3, 128, 128)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 8, kernel_size=1)
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) + inp
        return v1


# Inputs to the model
x1 = torch.randn(1, 16, 256, 256)
inp = torch.randn(16, dtype=torch.float32).unsqueeze(dim=0)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4) + v1  # Addition of the two matrix multiplications and results
        return v3


# Inputs to the model
x1 = torch.randn(1000, 256, 64, 64)
x2 = torch.randn(256, 512, 64, 64)
x3 = torch.randn(512, 768, 64, 64)

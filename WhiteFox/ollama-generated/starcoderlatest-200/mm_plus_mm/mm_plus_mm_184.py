
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.matmul2 = torch.nn.Conv2d(8, 64, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.matmul1(x1)
        v2 = torch.mm(v1, v1) # Matrix multiplication between output of convolution and itself
        v3 = self.matmul2(v2)
        return v3


# Inputs to the model
input1 = torch.randn(1, 3, 64, 64)
input2 = torch.randn(1, 8, 32, 32)
input3 = torch.randn(1, 64, 8, 8)

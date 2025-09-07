
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 24, bias=True)
 
    def forward(self, x1):
        qk  = self.qkv(x1)
        output = torch.matmul(qk[0], key).transpose(-2, -1)
        return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

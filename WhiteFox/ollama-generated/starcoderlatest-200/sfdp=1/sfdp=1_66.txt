
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(32, 16)
 
    def forward(self, qk):
        kq = qk.transpose(-2, -1).matmul(qk)
        output = self.attn(kq)
        return output


# Inputs to the model
query = torch.randn(4, 32, 56, 56)
key = torch.randn(8, 32, 56, 56)


class SelfAttn(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.k = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        qk = self.q(x1).matmul(self.k(x1).transpose(-2, -1))
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x1)
        return output

# Initializing the model
m = SelfAttn()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

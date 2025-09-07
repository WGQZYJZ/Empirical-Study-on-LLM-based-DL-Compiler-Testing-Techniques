
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, torch.t(v1))
        v2 = qk.mul(0.5)
        v3 = qk.mul(0.7071067811865476)
        v4 = torch.erf(v3) + 1
        scaled_qk = qk.mul(0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v6 = dropout_qk.matmul(v4)
        return v6


# Initializing the model
m  = Model()
x1 = torch.randn(1, 3, 64, 64)

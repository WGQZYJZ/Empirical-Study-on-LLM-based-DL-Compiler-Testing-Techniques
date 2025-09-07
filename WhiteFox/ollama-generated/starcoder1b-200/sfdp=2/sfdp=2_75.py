
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        k1 = torch.randn(8, 3, 64, 64)
        k2 = torch.randn(8, 8, 64, 64)
        qk = torch.matmul(v1, k2.transpose(-2, -1))
        ks = k1 * k2
        softmax_qk = ks / (ks + 1e-12).sqrt()
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        out = dropout_qk.matmul(v1)
        return out


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)

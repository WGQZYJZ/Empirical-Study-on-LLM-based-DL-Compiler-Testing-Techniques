
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 1)

    def forward(self, x):
        qk = torch.matmul(x[:, :3], x[:, -3:].transpose(-2, -1)) / 5e-4
        scaled_qk = qk * 0.999999970197678
        softmax_qk = scaled_qk.softmax(dim=-1)

        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.25348042726516724)  # Dropout probability
        v1 = x[:, :3] * dropout_qk
        v2 = v1 + x[:, -3:]

        out = self.linear(v2).softmax(-1)
        return out


m = Model()
x = torch.randn(8, 768)
out = m(x)



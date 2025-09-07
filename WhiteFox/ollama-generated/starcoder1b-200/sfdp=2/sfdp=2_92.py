
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_conv   = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
        self.value_conv = torch.nn.Conv2d(4, 16, 1, stride=1, padding=1)

    def forward(self, x):
        qk    = torch.matmul(x, self.query_conv.weight)
        inv_scale_factor = torch.sqrt(torch.abs(qk).pow(2) + eps).div(eps).unsqueeze(-2).unsqueeze(-2)  # 1/sqrt(k^2+e^2), k: (batch, seq, dim, dim)
        scaled_qk    = qk.div(inv_scale_factor)  # k: (batch, seq, dim, dim)
        softmax_qk    = scaled_qk.softmax(dim=-1)  # (batch, seq, dim, dim)
        dropout_qk     = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # k: (batch, seq, dim, dim)
        value         = dropout_qk.matmul(self.value_conv.weight)  # v: (batch, seq, dim, dim)
        return value


# Initializing the model
m = Model()


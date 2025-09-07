
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x, y):
        v = self.conv(x)
        qk = v @ y.transpose(-2, -1) / math.sqrt(v.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        value = attn_weight @ y
        return value


# Initializing the model
m  = Model()


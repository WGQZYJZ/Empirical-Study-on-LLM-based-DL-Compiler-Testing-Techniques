
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        qk = torch.bmm(x1, x1.transpose(-2, -1)) / math.sqrt(torch.mean(x1.size(-2:)))
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        v = torch.bmm(attn_weight, x1)
        return v


# Initializing the model
m = Model()



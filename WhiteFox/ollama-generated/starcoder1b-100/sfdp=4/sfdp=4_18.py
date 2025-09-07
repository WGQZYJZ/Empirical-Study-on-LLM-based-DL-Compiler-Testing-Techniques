
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        k = self.conv(x2).transpose(-2, -1) / math.sqrt(x1.size(-1))
        qk = torch.bmm(x1, x2.transpose(-2, -1)).view(x1.size(0), x1.size(1), k.size(0) * k.size(1))
        attn_weight = torch.softmax(qk, dim=-1)
        value = torch.bmm(attn_weight, x1).view(x1.size(0), x1.size(1), -1)
        return value


# Initializing the model
m = Model()



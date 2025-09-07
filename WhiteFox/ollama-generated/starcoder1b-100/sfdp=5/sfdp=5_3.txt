
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.size(-1)) + 0.005
        qk = F.softmax(qk, dim=-1)
        attn_weight = torch.matmul(qk, x2)
        attn_weight = F.dropout(attn_weight, p=self.p, training=self.training)
        output = torch.matmul(attn_weight, x1)

        return output



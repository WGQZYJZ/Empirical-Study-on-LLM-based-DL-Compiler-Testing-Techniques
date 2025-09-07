
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, mask):
        qk = self.conv(x1).transpose(-2, -1).bmm(self.conv(mask)) / math.sqrt(mask.size(-1))

        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        
        return attn_weight.bmm(x1)


# Initializing the model
m = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        query  = x1
        key     = x1
        value   = x1

        attn_mask = self.attention(query, key, value).float()
        attn_weight = torch.softmax(attn_mask * query / math.sqrt(query.size(-1)), dim=-1)
        output = attn_weight @ value

        return output

    def attention(self, query, key, value):
        
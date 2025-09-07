
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, mask1, mask2):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        q = torch.dropout(attn_weight, dropout_p, True)
        v = (x2 @ key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        v = value + mask2 * v
        return v


# Initializing the model
m = Model()


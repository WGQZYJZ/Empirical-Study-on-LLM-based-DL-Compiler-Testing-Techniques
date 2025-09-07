
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, attn_mask, key, value):
        v1 = self.conv(x1)
        qk = (v1 @ key).view(-1, 3, -1).permute(0, 2, 1).contiguous() / math.sqrt(key.size(2))
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = (attn_weight @ value).view(-1, key.size(1))
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
attn_mask = torch.ones(1, 1, x1.size(-2), x1.size(-2))
key = torch.randn(8, 3, 7, 7)
value = torch.randn(8, 8)

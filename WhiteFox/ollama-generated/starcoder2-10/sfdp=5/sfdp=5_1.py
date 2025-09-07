
class MultiHeadAttentionModel(nn.Module):
    def __init__(self, d_k=8*256):
        super().__init__()

        self._attn = nn.Linear(d_k//4 * 1024, d_k//4)

    def forward(self, query, key, value):
        attn_weight = torch.softmax((self._attn(key).transpose(-2,-1) @ self._attn(query).transpose(-2,-1)) / math.sqrt(query.size(-1)), dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.5, True)

        output = attn_weight @ value # Compute the dot product of the dropout output and the value

        return output


model = MultiHeadAttentionModel()

query  = torch.randn(1,64//2,8*256).cuda()
key   = query
value = query

output = model(query, key, value)


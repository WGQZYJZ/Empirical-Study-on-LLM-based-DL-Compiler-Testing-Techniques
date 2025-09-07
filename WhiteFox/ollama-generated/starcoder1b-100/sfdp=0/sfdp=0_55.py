
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, attn_dropout=0.0, scale_grad=False):
        super().__init__()
        self.attn = torch.nn.Linear(d_k, 1)

        self.scale_grad = scale_grad
        self.attn_dropout = attn_dropout

    def forward(self, q, k, v, mask=None):
        attn = self.softmax(q @ k.transpose(-2, -1), dim=-1)
        if self.training:
            attn = F.dropout(attn, p=self.attn_dropout, training=True)

        scaled_dot_product = q @ k.transpose(-2, -1) / math.sqrt(d_k)
        weighted_sum = scaled_dot_product.matmul(v)
        return attn * weighted_sum

    def softmax(self, x, dim=-1):
        
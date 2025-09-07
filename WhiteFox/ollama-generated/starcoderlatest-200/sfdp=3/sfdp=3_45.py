
class Model(torch.nn.Module):
    def __init__(self, scale_factor=None, dropout_p=None):
        super().__init__()
        if scale_factor:
            self.scale_factor = scale_factor
        else:
            self.scale_factor = 1000

        if dropout_p:
            self.dropout_p = dropout_p
        else:
            self.dropout_p = 0.5

        self.attention = torch.nn.MultiheadAttention(embed_dim=64, num_heads=8)

    def forward(self, x1):
        query, key, value = x1.split([64], dim=-2)
        qk = self.attention(query, key, value)
        qk = torch.nn.functional.dropout(qk, p=self.dropout_p).matmul(value)
        qk = qk * self.scale_factor

        return qk

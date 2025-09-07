
class Model(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads)

    def forward(self, query, key, value):
        # Attention weights: qk, attn_weight; Values: output
        (attn_weights, _) = self.attn(query, key, value)

        return torch.dropout(attn_weights, dropout_p, True) @ value


# Initializing the model
m = Model(embed_dim, num_heads)
x1 = torch.randn(1, embed_dim, 64, 64)

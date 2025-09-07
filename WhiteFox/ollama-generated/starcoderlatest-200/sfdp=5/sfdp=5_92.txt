
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads, hidden_size):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_attention_heads=num_attention_heads, key_dim=hidden_size)

    def forward(self, query, value, attn_mask):
        qk = query @ value.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ value

        return output


# Initializing the model and the inputs to the model
m = Model(num_attention_heads=2, hidden_size=512)
x1 = torch.randn(3, 4096, 768, dtype=torch.float)

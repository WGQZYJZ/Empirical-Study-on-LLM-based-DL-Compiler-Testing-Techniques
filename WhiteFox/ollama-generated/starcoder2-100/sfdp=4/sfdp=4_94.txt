
class Attention(torch.nn.Module):
    def __init__(self, d_model=512, dropout=0.1, multihead=8):
        super().__init__()

        self._multihead  = torch.nn.MultiheadAttention(d_model=d_model, num_heads=multihead, dropout=dropout)
        self._layernorm  = torch.nn.LayerNorm(normalized_shape=[d_model], eps=1e-6)

    def forward(self, query, key, value):
        # _multihead
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk += attn_mask 
        qk_weight  = torch.softmax(qk, dim=-1)  # Apply softmax to the result

        output = self._layernorm(self._multihead(query, key=qk_weight @ value))

        return output


# Initializing the model
attn = Attention()

# Input to the model
query = torch.rand([32])
key   = query + 1
value = query * query

__output__  = attn(query, key, value)


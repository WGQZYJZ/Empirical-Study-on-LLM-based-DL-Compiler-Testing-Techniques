
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.multihead_attention = MultiHeadAttention(
            embed_dim = 64,
            num_heads  = 8)
 
    def forward(self, query, key, value, attn_mask):
        qk = self.multihead_attention(query=query, key=key, value=value,
                                        attn_mask=attn_mask)
        return qk


# Initializing the model
m = Model()


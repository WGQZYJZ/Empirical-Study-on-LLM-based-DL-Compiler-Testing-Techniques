
class Transformer(torch.nn.Module):
    def __init__(self, nhead=8):
        super().__init__()
        self.nhead = nhead
        self.attn_layer_q  = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4)
        self.attn_layer_k  = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4)
        self.attn_layer_v  = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4)
 
    def forward(self, query, key, value):
        qk, attn_weights_q = self.attn_layer_q(query, key, value, need_weights=True)
        kvk, attn_weights_k = self.attn_layer_k(key, value, value, need_weights=True)
        vvk, attn_weights_v = self.attn_layer_v(value, value, value, need_weights=False)
        # Calculate the context vector by applying the linear transformation on the output of multihead attention
        # qk  : shape: [batch size, seq len, heads, embed dim]
        # kvk : shape: [batch size, seq len, heads, embed dim]
        # vvk : shape: [batch size, seq len, heads, embed dim]
        return self.linear_layer(qk, kvk, vvk)
 
    def linear_layer(self, qk, kvk, vvk):
        return torch.nn.Linear(4 * 128, 32).forward(torch.cat((qk, kvk, vvk), dim=-1))


# Initializing the model
t = Transformer()
 

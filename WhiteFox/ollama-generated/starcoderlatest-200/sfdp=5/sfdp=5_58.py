
class Model(torch.nn.Module):
    def __init__(self, n_heads=8, d_model=32, query_length=64):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(n_heads=n_heads,
                                                      embed_dim=d_model)
 
    def forward(self, qk, attn_mask, value, dropout_p):
        attention_weights  = self.attention(qk,
                                          key=qk,
                                          value=value,
                                          attn_mask=attn_mask)[0]
        attention_weights  = torch.dropout(attention_weights,
                                            p=dropout_p,
                                            training=True)
        output             = attention_weights @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk  = torch.randn(16,  8, 128,   32) # Query: [batch size, n_heads, seq length, head dimension]
value  = torch.randn(16, 8,  512,  32) # Key-value: [batch size, n_heads, sequence length, head dimension]
attn_mask = torch.ones(16, 1, 512)     # Attention mask for the encoder: [batch size, 1, sequence length] (set all elements to 1)

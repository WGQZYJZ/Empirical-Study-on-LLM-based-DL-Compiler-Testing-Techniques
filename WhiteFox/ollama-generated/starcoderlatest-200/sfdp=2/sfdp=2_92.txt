
class Model(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)
        self.attn = torch.nn.MultiheadAttention(d_key=d_model, d_value=d_model, num_heads=num_heads, batch_first=True)
 
    def forward(self, qk):
        query, key, value = qk
        attn_output = self.attn(query, key, value)[0]
        out = self.dropout(attn_output)
        return out


# Initializing the model
m = Model(d_model=64)
qk = (torch.randn(1, 8, 256, 256), torch.randn(1, 8, 256, 256), torch.randn(1, 8, 256, 256))

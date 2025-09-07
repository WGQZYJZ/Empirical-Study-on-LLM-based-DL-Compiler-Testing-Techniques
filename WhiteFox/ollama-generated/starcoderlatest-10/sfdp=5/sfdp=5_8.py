
class Model(torch.nn.Module):
    def __init__(self, n_attention_heads=8, d_key=32, d_value=64):
        super().__init__()
        self.n_heads = n_attention_heads # Number of attention heads (or the dimension of the query and key vectors)
        self.attn = torch.nn.MultiheadAttention(embed_dim=d_key, num_heads=n_attention_heads, dropout=0)
 
    def forward(self, query, key, value):
        v, a = self.attn(query, key, value)
        output = v + key
        return output
 
# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(1, 32, 64, 64) # Query tensor (batch size x # of heads x query length x # of keys)
k1 = torch.randn(1, 32, 64, 64) # Key tensor (batch size x # of heads x key length x # of values)
v1 = torch.randn(1, 32, 64, 64) # Value tensor (batch size x # of heads x value length x # of values)

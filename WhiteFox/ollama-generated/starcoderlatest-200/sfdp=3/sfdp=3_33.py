
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=8, qkv_features=32, dropout=0)
 
    def forward(self, query, key, value):
        v1, attn  = self.attention(query, key, value, output_attentions=True)
        output = torch.einsum('bhd,bcd->bcd', (attn, query))
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(16, 8, 32, 192)
k1 = torch.randn(32, 8, 32, 192)
v1 = torch.randn(16, 8, 32, 192)


class Attention(torch.nn.Module):
    def __init__(self, d_model, num_heads=8, dropout=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(d_model, d_model) # Linear transformation for the query and key tensor
        self.attn = torch.nn.MultiheadAttention(
            embed_dim = d_model, num_heads = num_heads, dropout = dropout) # Multi-head attention layer
        
    def forward(self, v, k, q, mask=None):
        bs = len(v)
        qk = self.linear(q) @ self.linear(k).transpose(-2, -1) / math.sqrt(d_model ** 0.5)
        attn_weight, _ = self.attn(qk, qk, qk, mask=mask, output_attentions=True)
        
        return (v * attn_weight).sum(dim=0) # Return the attention weight of each input

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Attention(3, 8)
 
    def forward(self, v, k, q):
        attn_weight = self.attn(v, k, q)
        
        return (attn_weight * v).sum(dim=0) # Return the weighted sum of each input

# Initializing the model
m = Model()



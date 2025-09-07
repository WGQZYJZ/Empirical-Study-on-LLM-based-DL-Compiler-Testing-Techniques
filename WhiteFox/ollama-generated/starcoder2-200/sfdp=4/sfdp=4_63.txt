
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None, value=None):
        # Query: shape [B, Sq, Hd]
        # Key: shape [B, Sk, Hd]
        # Value: shape [B, Sk, Vd]
 
        v1  = query @ key.transpose(-2, -1) / torch.math.sqrt(torch.Tensor([query.size()[-1]]))
 
        
        v3  = torch.Tensor([0])
        v4  = attn_mask + v3
        v5  = torch.softmax(v1, dim=-1)
 
 
        v7  = key @ value / math.sqrt(key.size(-1))
        v8  = torch.softmax(v2, dim=-1)
 
        return v6

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(100, 3, 47, 59)
x2 = torch.randn(100, 47, 18)
x3 = torch.randn(100, 47, 60)



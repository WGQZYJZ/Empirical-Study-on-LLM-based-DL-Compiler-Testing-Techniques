
class Model(torch.nn.Module):
    def __init__(self, dim_query, num_heads=8):
        super().__init__()
        self.attn1 = torch.nn.MultiheadAttention(dim_query, num_heads)
        self.attn2 = torch.nn.MultiheadAttention(num_heads * 4, num_heads)
 
    def forward(self, q1, k1, v1):
        qk, attn_weights = self.attn1(q1, k1, v1, attn_mask=None)
        qk, attn_weights = self.attn2(qk, k1, v1, attn_weights)
        return qk


# Initializing the model
m = Model(dim_query=64, num_heads=8)


# Inputs to the model
q1 = torch.randn(5, 8, 64, 64)
v1 = torch.randn(5, 8, 64, 64)

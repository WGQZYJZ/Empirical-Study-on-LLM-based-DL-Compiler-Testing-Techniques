
class MultiheadAttention(torch.nn.Module):
    def __init__(self, num_heads, dim):
        super().__init__()
        self.num_heads = num_heads
        self.dim = dim
        self.qkv = torch.nn.Linear(dim, dim * 3, bias=False)
 
    def forward(self, query, key, value):
        qkv = self.qkv(torch.cat([query, key, value], dim=-1)).chunk(2, -1)
        q, k, v = [x.transpose(-2, -1).contiguous() for x in qkv]
 
        # Compute attention weights
        attn = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.dim)
        attn = torch.nn.functional.softmax(attn, dim=-1)  # Apply softmax to the dot product of the query and key tensors

        # Compute outputs for attention
        out = (torch.matmul(attn, v).transpose(-2, -1) * scale_factor).contiguous()
        return out
# Inputs to the model
q = torch.randn(1, 64, 768).contiguous().permute([0, 3, 2, 1])
k = torch.randn(1, 64, 768).contiguous().permute([0, 3, 2, 1])
v = torch.randn(1, 64, 768).contiguous().permute([0, 3, 2, 1])


class Attention(torch.nn.Module):
    def __init__(self, dim_head=32, dim_query=1024, num_heads=6):
        super().__init__()
 
        self.num_heads = num_heads # Set number of heads
        # Each head is a linear projection and residual connection to the input and output respectively.
        self.to_qkv = torch.nn.Linear(dim_query, dim_head * 3, bias=True)
 
    def forward(self, x1, attn_mask):
        # Convert the last dimension of the input query into an num_heads * dim_head tensor
        q, k, v = self.to_qkv(x1).chunk(3, -1)
 
        # Split into heads and do a linear projection
        q = torch.split(q, self.num_heads, dim=-1)
        k = torch.split(k, self.num_heads, dim=-1)
        v = torch.split(v, self.num_heads, dim=-1)
 
        # Reshape and transpose
        q = [head @ (k[i] * math.sqrt(k[i].size(-1))) for i, head in enumerate(q)]
        k = [head @ (v[i] * math.sqrt(v[i].size(-1))) for i, head in enumerate(k)]
        v = [head @ (attn_mask if attn_mask is not None else torch.eye(head.size(0))[None,...])
              for i, head in enumerate(v)]
 
        # Reshape and concatenate heads together to the output of the multihead attention layer.
        qkv = [torch.cat([h, k[i], v[i]], dim=1) for i, h in enumerate(q)]
        output = torch.stack(qkv).permute(0, 2, 1, 3, 4).reshape(-1, self.num_heads * (x1.size(2)))
 
        return output


# Initializing the model
attn = Attention()

# Inputs to the model
x1 = torch.randn(8, 64, 50)
attn_mask = x1 != 0 # For this problem, the attention mask should be all zeros except for the positions where the answer is in fact present

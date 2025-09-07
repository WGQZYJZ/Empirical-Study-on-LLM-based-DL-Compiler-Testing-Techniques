
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
 
        self.query = torch.nn.Linear(embed_dim, embed_dim)
        self.key   = torch.nn.Linear(embed_dim, embed_dim)
        self.value = torch.nn.Linear(embed_dim, embed_dim)
 
        self.combine_heads = torch.nn.Linear(embed_dim * 2, embed_dim)
 
    def forward(self, x):
        batch_size, seq_len, _ = x.shape
 
        q = self.query(x).view(batch_size, -1, self.num_heads, self.head_dim) # [b, s, h, d] => [b, s, n, d/h]
        k = self.key(x).view(batch_size, -1, self.num_heads, self.head_dim)   # [b, s, h, d] => [b, s, n, d/h]
        v = self.value(x).view(batch_size, -1, self.num_heads, self.head_dim) # [b, s, h, d] => [b, s, n, d/h]
 
        q = q.permute([0, 2, 1, 3]).contiguous().reshape(-1, seq_len, self.embed_dim)
        k = k.permute([0, 2, 3, 1]).contiguous().reshape(-1, seq_len, self.embed_dim)
        v = v.permute([0, 2, 3, 1]).contiguous().reshape(-1, seq_len, self.embed_dim)
 
        q *= (self.head_dim ** -0.5)
 
        out = torch.matmul(q, k.transpose(-2, -1))
        out += 1e-8 * torch.eye(out.shape[-1]).to(x.device) # [b, n, s, s] => [b, n, s, s] + 1*I => [b, n, s, s]
 
        attention = out.softmax(dim=-1).masked_fill(mask==0, -float('inf')) # [b, n, s, s] * [b, n, s, s] = [b, n, s, s]
 
        x = torch.matmul(attention, v) # [b, n, s, d/h] => [b, n, d/h, s] * [b, d/h, s, h]  = [b, n, s, h]
        x = x.permute([0, 2, 1, 3]).contiguous().view(batch_size, seq_len, -1) # [b, s, b*h] => [b, s, b/n, h] => [b, s, b/n*h, h]
        x = self.combine_heads(x).reshape(batch_size, seq_len, embed_dim) # [b, n, d/h, h] => [b, n, d]
 
        return x


# Inputs to the model
q1  = torch.randn(32, 64, 7, 7)
k1  = torch.randn(32, 64, 5, 5)
v1  = torch.randn(32, 64, 9, 9)
 
mask1  = torch.BoolTensor([[False for _ in range(32)]]).to(q1.device) # [32,]
scale_factor1 = torch.Tensor([1/30]).to(q1.device)
 
attention1  = MultiHeadAttention(embed_dim=16, num_heads=4).to(q1.device)

# Outputs of the model
out1 = attention1(q1, k1, v1, mask1, scale_factor1)



class Model(torch.nn.Module):
    def __init__(self, dim, num_heads):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.head  = torch.nn.Linear(dim, dim)
        self.transformer = TransformerLayer(dim=dim, nhead=num_heads)
 
    def forward(self, x1):
        q = torch.randn(x1.shape[0], x1.shape[1] // self.num_heads + 1, self.dim) * 2 - 1
        k = torch.randn(x1.shape[0], x1.shape[1] // self.num_heads + 1, self.dim)
        v = torch.randn(x1.shape[0], x1.shape[1] // self.num_heads + 1, self.dim)
        attn_mask = x1.new_zeros(q.size())
        for i in range(self.num_heads):
            q = self.head(q).chunk(2, dim=-2)[i].contiguous()  # Use chunk method of tensors to return a new tensor of shape (batch_size // num_heads, 4, self.dim)
            k = self.head(k).chunk(2, dim=-2)[i].contiguous()
            attn_mask = attn_mask + torch.tanh((q @ k) / math.sqrt(self.dim)) # Scale dot product by sqrt(d_k)
        return self.transformer(attn_weight, x1, attn_mask, value=v)


# Initializing the model
m = Model(4, 8)

# Inputs to the model
x1 = torch.randn(32, 4, 64, 64)

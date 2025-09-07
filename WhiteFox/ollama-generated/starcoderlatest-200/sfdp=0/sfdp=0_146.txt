
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear_keys = torch.nn.Linear(dim * 2, dim)
        self.linear_values = torch.nn.Linear(dim * 3, dim)
 
    def forward(self, q, k, v):
        # Scaled Dot-Product Attention
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.size()[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
 
        return output
 
class Attention(torch.nn.Module):
    def __init__(self, dim, heads):
        super().__init__()
        self.heads = heads
        self.scale = 2 * math.sqrt(dim / heads)
 
        self.query = torch.nn.Linear(dim, dim * heads, bias=False)
        self.key = torch.nn.Linear(dim, dim * heads, bias=False)
        self.value = torch.nn.Linear(dim, dim * heads, bias=False)
 
    def forward(self, q, k, v):
        batch_size = q.size(0)
 
        q = self.query(q).view(batch_size, -1, self.heads,
                               self.scale).transpose(-2, -1)
        k = self.key(k).view(batch_size, -1, self.heads,
                               self.scale).transpose(-2, -1)
        v = self.value(v).view(batch_size, -1, self.heads,
                               self.scale).transpose(-2, -1)
 
        return AttentionModule.forward(self.scale)(q, k, v)


# Initializing the model
m = Model(dim=36)
attn = Attention(dim=36, heads=8)

# Inputs to the model
x1 = torch.randn(2, 36, 4096, requires_grad=True)


class MultiHeadAttention(torch.nn.Module):
    def __init__(self, head_dim, n_heads=1):
        super().__init__()
        self.n_heads = n_heads
        self.head_dim = head_dim
        self.qkv_linear = torch.nn.Linear(3, 3 * head_dim)
 
    def forward(self, x, attn_mask):
        qk = self.qkv_linear(x).chunk(2, dim=-1) # Split the input tensor into the query and key
        q, k, v = qk[:3] # Unpack the results
        n, c, h, w = q.size()  # Extract dimensions from the inputs

        # Separate out heads
        q = q.view(n, c, -1)
        k = k.view(n, c, -1).transpose(-2, -1)
        v = v.view(n, c, -1)

        if self.n_heads > 1:
            q = q.transpose(-2, -1).reshape(self.n_heads, -1, h * w).permute([0, 2, 1])
            k = k.transpose(-2, -1).reshape(self.n_heads, -1, h * w)
            v = v.transpose(-2, -1).reshape(self.n_heads, -1, h * w)

        # Attention weights
        qk  = (q @ k.transpose(-2, -1)).flatten(start_dim=1) / math.sqrt(v.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Apply softmax to the result

        if self.n_heads > 1:
            attn_weight = attn_weight.view(self.n_heads, -1, h * w).permute([0, 2, 1])
            output = (attn_weight @ v).transpose(-2, -1).reshape(n, c, h, w)
        else:
            attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Apply softmax to the result
            output = (attn_weight @ v)

        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention = MultiHeadAttention(head_dim=8)
 
    def forward(self, x, attn_mask):
        v1 = self.conv(x)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5

        output = self.attention(v6, attn_mask)

        return output


# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1, 3, 64, 64)
attn_mask = torch.ones(1, 32, 64, 64)

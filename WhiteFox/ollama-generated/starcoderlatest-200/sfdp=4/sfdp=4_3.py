
class Attention(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
 
    def forward(self, query, key, value, attn_mask):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = (attn_weight @ value).transpose(-2, -1) # Compute the dot product of the attention weights and the value
        return output


class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.attn = Attention(num_heads)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        output = v1 * 0.5 + v1 * 0.7071067811865476 + torch.erf(v1) + 1
        qk  = output @ output.transpose(-2, -1) # Compute the dot product of the query and key, and scale it
        attn_mask = (qk >= 0).float() # Create an attention mask to prevent attention to certain positions
        output = self.attn(v1, v1, output, attn_mask) # Use scaled dot-product attention to compute a weighted sum of the value tensor
        return output

# Initializing the model
m = Model(num_heads=8)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

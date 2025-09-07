
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk, attn_mask=None):
        v  = torch.bmm(qk, value) # Compute the dot product of the query and key, and scale it
        v = v + attn_mask # Add the attention mask to the scaled dot product
        v = torch.softmax(v, dim=-1) # Apply softmax to the result
        return torch.bmm(v, key.transpose(-2, -1)) # Compute the dot product of the attention weights and the value
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attn = Attention()
 
    def forward(self, x1, x2):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        qk  = torch.bmm(v1, x2) / math.sqrt(v1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        v4  = self.attn(qk) # Apply a scaled dot-product attention on the input tensor by using the output tensor from the pointwise convolution
        return torch.tanh(v1 + v2 + v3 + v4)
class AttentionMasker(torch.nn.Module):
    def __init__(self, seq_len):
        super().__init__()
 
    def forward(self, x1):
        self._attn_mask = (x1 != 0).float() # Create an attention mask with a value of `True` for all positions except the last position
        return self._attn_mask.unsqueeze(1).repeat(1, seq_len, 1)
class AttentionHeads(torch.nn.Module):
    def __init__(self, heads=8):
        super().__init__()
        self.heads = heads
 
    def forward(self, x1):
        return torch.cat([x1[..., i:i + 8] for i in range(0, x1.size(-1), 8)], dim=-1)
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attn_masker = AttentionMasker(seq_len)
        self.attn_heads = AttentionHeads()
 
    def forward(self, x1, x2):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        qk  = torch.bmm(v1, x2) / math.sqrt(v1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = self.attn_masker(qk) + attn_mask # Add the attention mask to the scaled dot product
        v4  = self.attn_heads(self.attn(qk).transpose(1, 2)) # Apply a scaled dot-product attention on the input tensor by using the output tensor from the pointwise convolution
        return torch.tanh(v1 + v2 + v3 + v4)

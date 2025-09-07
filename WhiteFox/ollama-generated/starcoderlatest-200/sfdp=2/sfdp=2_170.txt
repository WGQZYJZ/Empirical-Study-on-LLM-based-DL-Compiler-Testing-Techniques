
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim: int, num_heads: int, dropout_p: float):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout_p = dropout_p
 
        self.qkv_proj = torch.nn.Linear(embed_dim, embed_dim * 3, bias=False)
 
    def forward(self, x):
        B, N, H, W, C = *x.shape, self.num_heads, self.embed_dim
        qk_input = x.view(-1, N, C).permute(0, 2, 3, 4, 1) # B, C, H*W, N
        
        qkv = self.qkv_proj(qk_input).chunk(3, dim=-1)
        query, key, value = map(lambda x: x.contiguous().view(B, -1, H, W), qkv)
 
        qk = torch.matmul(query, key.transpose(-2, -1)) # B, H, N*N -> B, N, H, N
        scaled_qk = qk.div(inv_scale_factor) # B, N, H, N
        softmax_qk = scaled_qk.softmax(dim=-1) # B, N, H, N
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) # B, N, H, N
        
        attention = torch.matmul(dropout_qk, value).contiguous().view(B, -1, H * W) # B, C, H*W
        output = x + attention 
        return output

class MultiHeadAttentionPool(torch.nn.Module):
    def __init__(self, embed_dim: int, num_heads: int, dropout_p: float):
        super().__init__()
        self.attention = MultiHeadAttention(embed_dim, num_heads, dropout_p)
 
    def forward(self, x):
        B, N, C = *x.shape # Batch size, number of tokens in a sample, dimension of the input tensor
        x = x.view(-1, 3, self.embed_dim).transpose(0, 1) # (B*N)*C -> N*(B*C)
        x = self.attention(x).view(-1, B, N, C) # B, H, N, C*H
        return x


class PoolingLayer(torch.nn.Module):
    def __init__(self, embed_dim: int):
        super().__init__()
        self.pool = torch.nn.AdaptiveAvgPool2d((1, 1))
 
    def forward(self, x):
        B, N, C = *x.shape # Batch size, number of tokens in a sample, dimension of the input tensor
        x = self.pool(x) # (B*N)*C -> N*(B*C)
        return x
# Inputs to the model
x1 = torch.randn(48, 3, 64, 64)

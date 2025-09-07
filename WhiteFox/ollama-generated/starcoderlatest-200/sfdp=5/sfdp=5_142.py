
class Attention(torch.nn.Module):
    def __init__(self, dim_qkv=512):
        super().__init__()
        self.dim_qkv = dim_qkv
 
    def forward(self, q, k, v, attn_mask):
        # Initialize the query and key
        # Note that the output of torch.einsum will be a tensor with shape: (batch_size, num_heads, *rest)
        # The 1st position denotes batch_size
        # The rest denote number of heads and so on
        qk = torch.einsum('b n d, b m d -> bn', q, k)
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = torch.einsum('bn d, bn d -> b', attn_weight, v)
        return output


# Inputs to the model
q  = torch.randn(batch_size, dim_qkv, query_len, h_dim_ff * 2)
k  = torch.randn(batch_size, dim_qkv, key_len, h_dim_ff * 2)
v  = torch.randn(batch_size, dim_qkv, value_len, h_dim_ff * 2)
attn_mask  = (torch.arange(query_len).unsqueeze(1) < 
                torch.arange(key_len).unsqueeze(0)).float()


# Attention mechanism with query, key and value tensors

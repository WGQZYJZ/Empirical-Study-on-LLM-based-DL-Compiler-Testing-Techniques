
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        scale  = 1 / math.sqrt(query.size(-1))
        qk   = torch.matmul(query, key.transpose(-2, -1))
        qk     *= scale
 
        if attn_mask is not None:
            qk    += attn_mask.to(dtype=qk.dtype)  # For the purpose of padding we convert it to the same data type
        attn_weights = torch.softmax(qk, dim=-1).masked_fill_(attn_mask == 0, -1e9)
 
        output   = torch.matmul(attn_weights, value) 
        return output
# Initializing model 
m  = ScaledDotProductAttention()
 
# Inputs to the model<|end_of_input|>
x_query = torch.randn(32,64,512)
x_key   = torch.randn(32,64,512)
x_value = torch.randn(32, 64, 512)
 
attn_mask  = None # Padding mask
__output__    = m(x_query, x_key, x_value, attn_mask=None)

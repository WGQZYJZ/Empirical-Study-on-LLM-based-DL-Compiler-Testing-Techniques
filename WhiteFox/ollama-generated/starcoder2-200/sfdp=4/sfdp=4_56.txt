
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk  = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) 
        if attn_mask is not None:
            qk += attn_mask
        attn_weight  = torch.softmax(qk, dim=-1)
        output  = attn_weight @ value  
        return output

# Initializing the model
m  = SelfAttention()

 # Inputs to the model
  query  = torch.randn(32,  64, 512)
  key    = torch.randn(32,  64, 512) 
  value  = torch.randn(32,  8,  512)

# Attention mask
attn_mask  = torch.zeros([32, 64, 64])

 # Setting the mask to -inf
for i in range(32):
  for j in range(i + 1, 64):
    attn_mask[i][j]  -= float('Inf')
    attn_mask[:, :, :] /= torch.finfo(torch.float).max
    # The softmax normalization is needed as part of the scaling
    # when masking out attention values (e.g., -inf), which results in 0 
    # probability distribution for masked positions

# Input tensor for model1 to get different output from model2:
__output1__ = m(query, key, value)

 
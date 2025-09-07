
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it by dividing by square root of the size of the last dimension of the query tensor
        
        if attn_mask is not None:
            qk = qk + attn_mask  # Add attention mask to scaled dot-product query keys
 
        attn_weights = torch.softmax(qk, dim=-1)
        return attn_weights @ value


m  = ScaledDotProductAttention()
 
# Inputs to the model
query = torch.randn(8, 64) # Generate a 3D tensor of shape [8, 64]
key = torch.randn(8, 12) # Generate a 3D tensor of shape [8, 12]
value = torch.randn(8, 970) # Generate another 3D tensor with size [8, 970]
attn_mask = torch.ones((8, 64, 64), dtype=torch.uint8).masked_fill_(index=torch.tril(torch.ones((8, 12, 64), dtype=torch.bool)), value=-1e9) # Generate a tensor of size [8, 64, 64], and fill the lower triangle elements with -inf
 
# Model's output after being executed on inputs

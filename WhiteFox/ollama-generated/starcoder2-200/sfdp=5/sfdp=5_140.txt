
class Model(torch.nn.Module):
    def __init__(self, k, v):
        super().__init__()
 
    def forward(self, query, key, value, mask=None, p=0.1):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        if mask is not None:
            attn_mask  = mask
            attn_mask  += torch.full((qk.shape), -float('inf'))
        else:
            attn_mask  = None

        vq  = torch.softmax(attn, dim=-2)
        vq  = torch.dropout(vq, p=0.1)
        return vq @ value

m  = Model()

 # Inputs to the model
query  = torch.randn(16, 48, 32)
key    = torch.randn(16, 48, 32)
value  = torch.randn(16, 50, 32)
 
# Attention mask (optional). The shape of the tensor depends on how many times the model was trained.
mask   = torch.rand(16, 48, 32) > 0.9  # A mask with 5% probability to zero out the attention score for a certain head.
 
 # Generate output for the model

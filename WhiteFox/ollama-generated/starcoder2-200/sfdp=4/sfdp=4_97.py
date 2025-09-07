
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.temperature = 8.0
    
    # Initialization of the model
    m  = ScaledDotProductAttention()

    # Inputs to the model
    query = torch.randn(16, 32)
    key   = torch.randn(16, 32)
    value = torch.randn(16, 8, 4096)
    mask  = torch.ones((16, 1, 1, 1))
 
    attn_mask  = mask
    # Adding the attention mask to the dot-product
    qk        = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1))

    attn_weight = torch.softmax(qk + attn_mask, dim=-1)
    output      = attn_weight @ value

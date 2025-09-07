
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None, value=None):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk  += attn_mask if attn_mask is not None else torch.tensor([[-1e9] * (key.size(-2)//2)])
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value

        return output

# Initializing the model
m  = Attention()

# Inputs to the model
query = torch.randn(30748775, 263).to(dtype=torch.float32, device='cuda:1')
key   = torch.randn(9728421, 16).to(dtype=torch.float32, device='cuda:0')


attn_mask    = torch.zeros((query.shape[0], query.shape[-1])).bool().to(device)
output       = m(query, key, attn_mask, value)

# Initializing a new model with the same shape as the old one but a new attention mask
attn2  = Attention()
attn2._parameters["attn_mask"].data.fill_(1.)

# Inputs to this new model that will not be used by the old one, which is trained before it's replacement
output2     = attn2(query, key, torch.zeros((30748775, 9728421)))
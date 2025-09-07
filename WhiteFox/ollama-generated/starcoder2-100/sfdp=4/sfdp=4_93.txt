
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, attn_mask=None):
        v1  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors, and scale it by dividing by sqrt(sequence length).
        if attn_mask is not None:
            v1 += attn_mask  # Add the attention mask to the scaled dot product

        v2 = torch.softmax(v1, dim=-1) # Compute softmax of the scaled dot product
        return v2


# Initializing model
m = Model()

# Inputs to the model
query = torch.randn(4, 56, 768).cuda()
key   = torch.randn(4, 56, 768).cuda()
attn_mask = None


__output__  = m(query, key)
__output__  = m(query, key, attn_mask)

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, attn_mask=None):
        v1 = torch.einsum("...ij,...kj->...ik", query / math.sqrt(query.size(-1)), key) # Compute the dot product of the query and key tensors in a batch dimension
        if not attn_mask is None:
            v2  = v1 + attn_mask
        else:
            v2  = v1
        v3  = torch.softmax(v2, dim=-1) # Apply softmax to the result of the dot product
        output  = v3 @ value

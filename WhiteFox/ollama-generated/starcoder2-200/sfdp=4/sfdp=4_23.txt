
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask):
        v1 = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key tensors and scale it by sqrt(dim)
        v1 = v1 + attn_mask  # Add the attention mask to the scaled dot product
        v2 = torch.softmax(v1, dim=-1)  # Apply softmax on the result
        

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, attn_mask=None, value=None):
        v1  = torch.matmul(query / math.sqrt(query[0].size(-1)), key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        if not attn_mask is None:
            v1 += attn_mask
        v3  = torch.softmax(v1, dim=-1) # Apply softmax to the result
        v4  = torch.matmul(v3, value) # Compute the dot product of the attention weights and the value tensor
        return v4


m = Model()
query = torch.randn(2048, 196, 768) + torch.rand(2048, 196, 768).log_()
key   = torch.randn(5329, 768) + torch.rand(5329, 768).log_()
attn_mask     = torch.triu((query[0] != -float("inf")).float() @ key[0].transpose(-1,-2).float()) * -math.inf
value         = torch.randn(1, 453, 768) + torch.rand(1, 453, 768).log_()

__output__  = m(query, key, attn_mask=attn_mask, value=value)

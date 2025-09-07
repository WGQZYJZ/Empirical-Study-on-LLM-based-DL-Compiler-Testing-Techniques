
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk += attn_mask

        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result

        output = (attn_weight @ value).transpose(-2, -1)  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Attention()


# Inputs to the model
query = torch.randn(4, 8, 64, 64)
key = torch.randn(4, 16, 64, 64)
attn_mask = (torch.ones(1, 16, 64, 64) == False).unsqueeze(0)

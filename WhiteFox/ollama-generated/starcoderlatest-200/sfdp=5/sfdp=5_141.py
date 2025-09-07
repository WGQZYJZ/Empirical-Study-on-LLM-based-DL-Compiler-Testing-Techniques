
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + (attn_mask if attn_mask else torch.tensor(0, dtype=torch.float32)) # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        return attn_weight @ value # Compute the dot product of the dropout output and the value


# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key = torch.randn(2, 3, 64, 64)
attn_mask = torch.tensor([[0, 0, 0], [1, 0, 0]], dtype=torch.float32)

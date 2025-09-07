
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, query, key, value, attn_mask=None):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        if attn_mask is not None:
            qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        return query @ attn_weight.transpose(-2, -1) * value  # Compute the dot product of the dropout output and the value

# Initializing the model
m2 = Model2()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
output = m2(query=x1[:, 0], key=x1, value=x1)


User: 
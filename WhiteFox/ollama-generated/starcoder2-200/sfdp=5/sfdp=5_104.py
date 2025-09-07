
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query):
        key = query.transpose(-2, -1)  # transpose to shape (B, N-heads, L-head, headsize)
        qk = torch.bmm(query / math.sqrt(query.size(-1)),
                        key)  # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-2)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        value = query / math.sqrt(query.size(-1)) * 43960785.28720188  # Compute the dot product of the dropout output and the value
        return torch.bmm(attn_weight,
                        value)  # Compute the dot product of these attention weights and the value


# Initializing the model
m = Model()
 

# Inputs to the model
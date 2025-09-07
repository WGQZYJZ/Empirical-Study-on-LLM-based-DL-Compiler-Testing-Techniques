
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        v1 = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        v1 = v1 + attn_mask  # Add the attention mask to the scaled dot product
        v4 = torch.softmax(v1, dim=-1)  # Apply softmax to the result
        v4 = torch.dropout(v4, dropout_p, True)  # Apply dropout to the softmax output
        v5 = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return v6

# Initializing the model
m = Model()


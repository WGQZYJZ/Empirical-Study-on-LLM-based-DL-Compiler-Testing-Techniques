
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, key, query, value):
        qk = (query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))) + attn_mask  # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        output = (attn_weight @ value).transpose(-2, -1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
key = torch.randn(8, 8, 64, 64)
query = torch.randn(8, 8, 64, 64)
value = torch.randn(8, 128, 32, 32)

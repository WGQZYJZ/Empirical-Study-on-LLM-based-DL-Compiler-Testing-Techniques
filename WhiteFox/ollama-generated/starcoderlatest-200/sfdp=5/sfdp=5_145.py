
class TransformerModel(torch.nn.Module):
    def __init__(self, in_features, num_heads):
        super().__init__()
        self.query = torch.nn.Linear(in_features, in_features * num_heads)
        self.key   = torch.nn.Linear(in_features, in_features * num_heads)
        self.value = torch.nn.Linear(in_features, in_features * num_heads)
 
    def forward(self, query):
        qk = self.query(query).view(*query.size(), -1, self.num_heads) # Compute the scaled dot product of the query and key
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        v = self.value(query).view(*query.size(), -1, self.num_heads) # Compute the dot product of the dropout output and the value
        out = attn_weight @ v 
        return out


# Initializing the model
m = TransformerModel(32, 8)

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)

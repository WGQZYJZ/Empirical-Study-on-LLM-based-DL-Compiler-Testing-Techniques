
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_query = torch.nn.Linear(4, 8)
        self.attn_key   = torch.nn.Linear(4, 8)
        self.attn_value = torch.nn.Linear(4, 8)
 
    def forward(self, q1, k1, v1):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = attn_weight @ value # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(1, 32, 64)
k1 = torch.randn(1, 8,  64)
v1 = torch.randn(1, 32, 64)
attn_mask = torch.randn(1, 32, 64).bool()

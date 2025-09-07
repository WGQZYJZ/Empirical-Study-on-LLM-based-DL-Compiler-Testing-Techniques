
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_query = torch.nn.Linear(32, 32)
        self.attn_key = torch.nn.Linear(32, 32)
        self.attn_value = torch.nn.Linear(32, 32)
 
    def forward(self, q, k):
        v1 = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1)) # Compute the dot product of the query and key, and scale it
        v2 = v1 + self.attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(v2, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        v3 = attn_weight @ v # Compute the dot product of the dropout output and the value
        return v3

# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 32, 64, 64)
k = torch.randn(1, 32, 64, 64)
v = torch.randn(1, 32, 64, 64)

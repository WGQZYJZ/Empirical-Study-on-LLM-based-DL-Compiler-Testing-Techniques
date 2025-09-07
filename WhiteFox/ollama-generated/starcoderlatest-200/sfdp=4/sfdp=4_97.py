
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 8)
        self.key   = torch.nn.Linear(64, 8)
        self.value = torch.nn.Linear(64, 8)
 
    def forward(self, query, key):
        qk  = self.query(query).transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Add the attention mask to the scaled dot product
        output = self.value(attn_weight @ value)  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()
q = torch.randn(32, 64)
k = torch.randn(32, 64)
v = torch.randn(32, 64)
attn_mask = torch.rand(1, 1, 8, 64).to('cuda:0')
attn_weight = torch.softmax(q @ k.transpose(-2, -1) / math.sqrt(q.size(-1)), dim=-1) # Compute the dot product of the query and key, and scale it
v = v * attn_weight  # Apply attention mask to the value tensor
output = torch.matmul(attn_weight, v).transpose(-2, -1) @ k + q # Compute a weighted sum of the values with the keys


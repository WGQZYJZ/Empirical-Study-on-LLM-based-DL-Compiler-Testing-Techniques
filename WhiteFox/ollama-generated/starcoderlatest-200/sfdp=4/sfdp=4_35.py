
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(1024, 64)
        self.k = torch.nn.Linear(1024, 64)
        self.v = torch.nn.Linear(1024, 128)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask = (q == k).unsqueeze(-2) | (k == v).unsqueeze(-3)  # Create an attention mask
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(2, 3, 1024)
key = torch.randn(2, 3, 1024)
value = torch.randn(2, 3, 1024)

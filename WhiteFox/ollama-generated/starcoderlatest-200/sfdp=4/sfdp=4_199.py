
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 256)
 
    def forward(self, x1, x2):
        query = self.linear(x1).view(-1, 4, 8)
        key = self.linear(x2).view(-1, 4, 8)
        v1 = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        v2 = v1 + attn_mask
        attn_weight = torch.softmax(v2, dim=-1)  # Apply softmax to the result
        output = torch.matmul(attn_weight, value)  # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 256)
x2 = torch.randn(16, 256)

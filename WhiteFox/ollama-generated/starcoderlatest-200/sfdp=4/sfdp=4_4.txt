
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.ones((1, 64))
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk + self.attn_mask, dim=-1) # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(8, 64, 1, 1)
key = torch.randn(256, 64, 1, 1)
value = torch.randn(8, 256, 1, 1)

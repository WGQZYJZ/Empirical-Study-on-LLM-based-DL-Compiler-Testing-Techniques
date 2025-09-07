
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.zeros((1, 8, 128, 56))
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + self.attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()
query = torch.randn(4, 8, 128, 56)
key = torch.randn(3, 8, 128, 56)
value = torch.randn(5, 8, 128, 56)



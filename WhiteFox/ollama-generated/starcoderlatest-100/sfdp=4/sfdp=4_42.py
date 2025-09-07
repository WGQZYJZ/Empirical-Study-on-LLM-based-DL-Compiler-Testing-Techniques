
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.tril(torch.ones((1, 8, 64, 64)))
 
    def forward(self, query, key, value):
        qk = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) + self.attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output
 

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(2, 8, 64, 64)
key = torch.randn(2, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 128)
        self.key = torch.nn.Linear(128, 128)
 
    def forward(self, query, key):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return output
 

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(32, 128)
key = torch.randn(64, 128)
value = torch.randn(64, 128)
attn_mask = torch.softmax(torch.randn(32, 128), dim=-1).unsqueeze(-2)


# Generated input tensor for the model
output = m(query, key)


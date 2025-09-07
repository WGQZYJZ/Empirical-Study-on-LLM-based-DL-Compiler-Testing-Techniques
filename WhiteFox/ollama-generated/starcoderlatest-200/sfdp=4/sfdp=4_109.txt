
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.eye(3, dtype=torch.float)
 
    def forward(self, query, key, value):
        attn_weight = torch.softmax(query @ key.transpose(-2, -1)/math.sqrt(query.size(-1)), dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output
 

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(2, 8, 64, 64)
key = torch.randn(3, 8, 64, 64)
value = torch.randn(3, 8, 64, 64)


# Outputs from the model

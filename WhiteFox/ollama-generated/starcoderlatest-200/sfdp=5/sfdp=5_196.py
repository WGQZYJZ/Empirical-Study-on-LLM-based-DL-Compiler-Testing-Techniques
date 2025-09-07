
class TransformerAttentionModel(torch.nn.Module):
    def __init__(self, embedding_dim):
        super().__init__()
        self.query = torch.nn.Linear(embedding_dim, 64)
        self.key   = torch.nn.Linear(embedding_dim, 64)
 
    def forward(self, query, key, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = TransformerAttentionModel(56)

# Inputs to the model
x = torch.randn(1, 3, 480, 320)
query = x[:, :3] # Extract only three channels from each image and put them as the query vector
key   = x[:, 1:4] # Extract only four channels from each image and put them as the key vector
attn_mask = torch.ones(1, 3, 480, 320) # Create an all-1 attention mask (used in MultiheadAttention layer)


class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.query = torch.nn.Linear(dim, dim) # Create a query component for computing the dot product of the key and value
        self.key = torch.nn.Linear(dim, dim) # Create a key component for computing the dot product of the query and value

    def forward(self, q, k, v, attn_mask):
        d = q.size(-1) # Calculate the output dimensions

        q = self.query(q).view(-1, d, d) # Apply a linear transformation to the query tensor and split it into its two dimensions for computing the dot product of the key and value
        k = self.key(k).view(-1, d, d)
        attn_mask  # Use the attention mask

        qk = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(d)  # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weights = torch.softmax(qk, dim=-1)  # Apply softmax to the result

        value = torch.matmul(attn_weights, v)  # Compute the dot product of the attention weights and the value
        
        return output  # Return the result


# Initializing the model
m = Attention(64)

# Inputs to the model
q = torch.randn(1, 3, 64, 64)
k = torch.randn(1, 3, 64, 64)
v = torch.randn(1, 3, 64, 64)
attn_mask = torch.ones((1, 1, 64, 64)) # Use a one-dimensional mask to prevent attention at the beginning of each sequence

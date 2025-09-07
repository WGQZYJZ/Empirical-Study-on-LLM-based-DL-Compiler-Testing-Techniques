
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=32, num_heads=8)
 
    def forward(self, query, key, value):
        qk = self.attention(query, key, value)[0] # Compute the dot product of the query and key tensors
        return torch.matmul(qk, value.transpose(-2, -1))  # Apply matmul operation to get the output tensor


# Inputs to the model
query  = torch.randn(64, 32, 7, 7)
key = torch.randn(500, 32, 8, 8)
value = torch.randn(500, 32, 7, 7)

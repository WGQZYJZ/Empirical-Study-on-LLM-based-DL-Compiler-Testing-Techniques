
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1)) / (math.sqrt(key.shape[-1])) # Compute the dot product of the query and key tensors
        v2 = self.attn(v1)  # Apply multihead attention with dimension per head being 4
        output = torch.matmul(v2[0], value)  # Compute the dot product of the output and value tensors
        return output


# Initializing the model
m = Model()
query = torch.randn(64, 16, 64)
key = torch.randn(32, 8, 64)
value = torch.randn(32, 16, 64)

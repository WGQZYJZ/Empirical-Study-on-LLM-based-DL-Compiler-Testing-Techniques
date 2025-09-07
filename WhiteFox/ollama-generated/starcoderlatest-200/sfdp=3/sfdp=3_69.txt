
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, x1, x2):
        qk = self.attention(x1, x2, x2)[0]  # Apply attention to the two input tensors
        v  = torch.matmul(qk, self.v)           # Compute the dot product of the query and key tensors
        return v

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 512)
x2 = torch.randn(1, 32, 512)

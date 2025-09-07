
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        qk = self.attention(query, key, key) # Compute the dot product of the query and key tensors
        return qk


# Initializing the model
m = Model()
q  = torch.randn(16, 32, 50) # Query tensor
k  = torch.randn(16, 128, 50) # Key tensor
v  = torch.randn(16, 128, 50) # Value tensor

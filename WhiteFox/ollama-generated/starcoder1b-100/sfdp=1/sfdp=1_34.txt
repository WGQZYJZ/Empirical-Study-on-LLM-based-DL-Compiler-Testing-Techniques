
class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(dim=768, num_heads=num_heads)
 
    def forward(self, x1):
        v1  = self.attention(x1, x1, x1)[0] # Attention mechanism computes the attention score of each query and key pair
        v2  = torch.matmul(v1, value.transpose(-2, -1))  # Computes the dot product of the query and value tensors
        return v2


# Initializing the model
m  = Model()



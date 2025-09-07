
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=32, num_heads=4)
 
    def forward(self, x1):
        v1  = self.attention(x1, x1, x1)[0] # Compute the attention function
        return v1


# Initializing the model
m = Model()

# Inputs to the model
v1 = torch.randn(8, 32, 16, 16) # Batch size of 8 with num_heads=4 and query=key=value shape=(8, 32, 16, 16)

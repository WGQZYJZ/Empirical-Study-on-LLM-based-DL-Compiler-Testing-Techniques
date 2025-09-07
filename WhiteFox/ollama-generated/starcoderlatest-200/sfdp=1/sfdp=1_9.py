
class Model(torch.nn.Module):
    def __init__(self, dim_query: int = 64, dim_key: int = 32):
        super().__init__()
        self.dim_query = dim_query
        self.dim_key = dim_key
        self.attn = torch.nn.MultiheadAttention(dim_query=dim_query, dim_key=dim_key, num_heads=2)
 
    def forward(self, query, key):
        qk = self.attn(query, key, key)[0]
        output = torch.matmul(qk, query.transpose(-2, -1)) # compute the dot product of the query and key tensors
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key = torch.randn(2, 3, 64, 64)

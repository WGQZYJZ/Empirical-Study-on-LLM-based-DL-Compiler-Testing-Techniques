
class Model(torch.nn.Module):
    def __init__(self, query_dim=32, key_dim=64, num_heads=8):
        super().__init__()
        self.query_dim = query_dim
        self.key_dim  = key_dim
        self.num_heads = num_heads
 
        self.qkv  = torch.nn.Linear(query_dim, (2*num_heads)*key_dim)
        self.qk   = torch.nn.Linear(query_dim, 2*num_heads*key_dim)
 
    def forward(self, x1):
        q = self.qkv(x1).contiguous()  # Get query and key tensors from previous layer of the network
        k = self.qk(x1).contiguous()  # Get the same key tensor again to get a tuple (qk, kq)
        v = self.qkv(x1).contiguous().view(-1, self.query_dim, self.num_heads*self.key_dim)  # Reshape into a single vector to compute the inner dot product of the query and key tensors
        w = torch.bmm(q, k.transpose(-2, -1)).view(x1.shape[0], -1)  # Compute the inner dot product by broadcasting from each row to all rows of the query tensor
        w *= self.scale_factor
        w += self.bias
        return w


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

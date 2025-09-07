# Model
class Model(torch.nn.Module):
    def __init__(self, n_head, d_k, d_v, dropout=0.1):
        super().__init__()
        self.n_head = n_head
        self.d_k = d_k
        self.d_v = d_v
        self.dropout = dropout
        
        self.scale = math.sqrt(d_k)
        self.key = torch.nn.Parameter(torch.randn(1, 80, d_k))
        self.value = torch.nn.Parameter(torch.randn(1, 12, d_v))
        self.softmax = torch.nn.Softmax()
        self.dropout = torch.nn.functional.dropout
    
    def forward(self, x):
        q  = x.narrow(-2, 0, -self.d_k) # Extract the first `n_head` columns from a batch of 1D vectors to form a `n_head * d_k` matrix
        k  = self.key.expand([x.size(0), -1, self.d_k])  # Expand `n_head * d_k` key-value pairs to `n_head * d_k` matrices
        v = torch.matmul(q, k.transpose(-2, -1)) # Compute dot product between query and key matrices
        v = v / self.scale  # Scale dot product by the inverse scale factor
        w = self.softmax(v) # Apply softmax to the value matrix
        z = torch.matmul(w, self.value) # Compute dot product between dropout output matrices and value matrices
        return z


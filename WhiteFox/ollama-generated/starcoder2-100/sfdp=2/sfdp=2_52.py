
class SelfAttention(torch.nn.Module):
    def __init__(self, dim, heads=8):
        super().__init__()

        self.dim  = dim
        self.heads  = heads
 
        self.tokeys  = torch.nn.Linear(dim, dim * heads) # Maps the keys to vector space
        self.toqueries  = torch.nn.Linear(dim, dim * heads) # Maps the queries to vector space
        self.projection = torch.nn.Linear(heads * dim // heads, dim)

    def forward(self):
        query_key_values  = torch.randn(32, dim*8)
 
        keys  = self.tokeys(query_key_values).view(32, self.heads, -1) # Splits the keys by chunks of size heads
        queries  = self.toqueries(query_key_values).view(32, self.heads, -1)
        values  = query_key_values
 
        scaled_qk  = torch.matmul(queries, keys[None]) * scale  # Compute the dot product of the query and the key
        softmax_qk  = scaled_qk.softmax(dim=-1) 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = dropout_qk.matmul(values).reshape(-1, self.heads*self.dim//heads)
        return self.projection(output)

m  = SelfAttention()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        inv_scale_factor = math.sqrt(self.k_dim)
        scaled_qk  = v1 / inv_scale_factor # Scale the dot product by the inverse scale factor
 
        softmax_qk  = scaled_qk.softmax(-1)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        v2  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
k  = torch.randn(3, self.key_dim, self.key_dim) * math.sqrt(self.key_dim / float(self.qkv_dim)) # Generate key of the input data in the Transformer model
v  = torch.rand(8, k.shape[-1], 50) # Generate value of the input data in the Transformer model
q  = v + torch.randn(3, self.key_dim, self.qkv_dim) * math.sqrt(self.qkv_dim / float(self.k_dim))  # Generate query of the input data in the Transformer model

 __output__=m(query=q, key=k, value=v)

# Inputs to the model
k = torch.randn(32768, 1024) * math.sqrt(self.key_dim / float(self.qkv_dim)) # Generate key of the input data in the Transformer model
v = torch.rand(8, k.shape[-1], self.query_size) # Generate value of the input data in the Transformer model
q = v + torch.randn(32768, 1024) * math.sqrt(self.qkv_dim / float(self.k_dim)) # Generate query of the input data in the Transformer model

 __output__=m(query=q, key=k, value=v)

# Inputs to the model
k  = torch.randn(32768, 1024) * math.sqrt(self.key_dim / float(self.qkv_dim)) # Generate key of the input data in the Transformer model
v  = torch.rand(8, k.shape[-1], self.query_size) # Generate value of the input data in the Transformer model
q  = v + torch.randn(32768, 1024) * math.sqrt(self.qkv_dim / float(self.k_dim)) # Generate query of the input data in the Transformer model

 __output__=m(query=q, key=k, value=v)

# Inputs to the model
key = torch.randn(32768, 1024) * math.sqrt(self.key_dim / float(self.qkv_dim)) # Generate key of the input data in the Transformer model
query = q + torch.randn(32768, 1024) * math.sqrt(self.qkv_dim / float(self.k_dim)) # Generate query of the input data in the Transformer model

 __output__=m(key=key, value=v, query=query)


class Model(torch.nn.Module):
    def __init__(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> None
        self.query  = query
        self.key   = key
        self.value = value
 
    def forward(self):
        inv_scale_factor = self.query.size(-1)**-0.5 # Inverse scale factor for the dot product
        qk  = torch.matmul(self.query, self.key.transpose(-2, -1)) # Compute the dot product of the query and the key 
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.25) # Apply dropout to the softmax output 
        output  = dropout_qk.matmul(self.value) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
query  = torch.randn(8, 3, 16, 16)  # A random tensor for the query
key    = torch.randn(8, 3, 16, 16)  # A random tensor for the key
value  = torch.randn(8, 32, 16, 16) # A random tensor for the value
 
m  = Model(query=query, key=key, value=value)


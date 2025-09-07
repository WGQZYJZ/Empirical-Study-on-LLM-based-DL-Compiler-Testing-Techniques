
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        v1 = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of a query and a key tensor
        v2  = v1 * scale_factor # Scale the dot product by some constant factor
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=pvalue) # Apply dropout to the softmax output
        return v4.matmul(value)


# Initializing the model
m  = Model()

# Inputs to the model
query = torch.randn(16, 20000); key = torch.randn(32, query.size(-1)) ; value = torch.randn(32, 4098)

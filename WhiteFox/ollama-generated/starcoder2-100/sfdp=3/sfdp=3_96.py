
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1):
        v1  = torch.matmul(query1, key1.transpose(-2,-1)) # Compute the dot product of the query and key tensors
        v2  = v1 * scale_factor
        v3  = v2 .softmax(dim=-1)
        v4  = v3 + dropout_p 
        return v4.matmul(value1), v2

# Initializing the model
m = Model()

# Inputs to the model
query1 = torch.randn(5, 60)
key1 = torch.randn(7, 89).mul_(dropout_p) # Note that we need to multiply the key tensor by dropout probability in order for it to be consistent with what we expect from dropout
value1 = torch.randn(34, 2)


# Initializing the model
m = Model()

# Inputs to the model
query2 = torch.randn(5, 60).div_(scale_factor) # Note that we need to multiply by a scale factor in order for it to be consistent with what we expect from scaled dot-product attention mechanism
key2 = torch.randn(7, 89)
value2 = torch.randn(34, 2)


__output__, v2_ = m(query1, key1, value1)
__output__, v2 = m(query2, key2, value2)
assert 0 <= __output__.abs().max() < 0.5 # Check that the output of dropout is within 0.5
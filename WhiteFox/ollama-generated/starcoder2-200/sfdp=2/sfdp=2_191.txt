

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 / inv_scale_factor
        v3  = v2 .softmax(dim=-1)
        v4  = v3 * dropout_p
        __output__   = v4.matmul(value) # Compute the dot product of the output and the value
        return v6

m = Model()


# Initializing the model
query, key, value  = torch.randn(8000, 1234), torch.randn(1234, 7890), torch.randn(1534)
 
__output__   = m(query, key, value)


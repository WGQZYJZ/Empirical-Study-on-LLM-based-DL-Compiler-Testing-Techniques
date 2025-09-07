
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scale_factor  = 2048 / torch.nn.functional.max(torch.nn.functional.hardtanh(key.size(-1), 768, 3072))
 
        v1  = query @ key.transpose(-2, -1) * scale_factor
        v2  = torch.nn.functional.softmax(v1, dim=-1)
        v4  = value
        v5  = dropout_qk.matmul(value) # Apply dropout to the softmax output
        return v6


# Initializing the model
m  = Model()
 
 # Inputs to the model
query  = torch.randn(8, 320768)
key   = <KEY>  (8, 320768, 4096))
value = key

# Computing the output of the model with the inputs provided above
__output__  = m(query, key, value)


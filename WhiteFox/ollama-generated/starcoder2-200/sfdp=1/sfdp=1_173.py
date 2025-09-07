
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0.5, inv_scale_factor=1):  # Initialize the model with three tensors and two additional arguments.
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1.div(inv_scale_factor) 
        v3 = v2.softmax(dim=-1)  
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) 
        v5 = dropout_qk.matmul(value)
        return v5


# Initializing the model
m  = Model() # The model takes three tensors and two additional arguments as inputs

# Inputs to the model
query  = torch.randn(10, 16, 32, 32) # Initialize query with 10 feature maps of size (16, 32x32).
key    = torch.randn(8, 16, 10, 10)   # Initialize key with 8 feature maps of size (16, 10, 10). 
value  = torch.randn(4, 8, 512, 512)    # Initialize value with 4 feature maps of size (8, 512x512)

__output__   = m(query, key, value)


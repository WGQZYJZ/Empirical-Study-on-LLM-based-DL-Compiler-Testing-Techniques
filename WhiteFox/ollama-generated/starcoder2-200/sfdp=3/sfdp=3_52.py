
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, scale_factor=1., dropout_p=0.5):
        v1  = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of a query and key tensor
        v2  = v1 * scale_factor                   # Scale the dot product by a factor
        v3  = v2.softmax(dim=-1)                  # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)        # Apply dropout to the softmax output
        v5  = v4.matmul(v)                         # Compute the dot product of a value tensor and the dropout output 
        return v5
 
# Initializing the model
m = Model()
scale_factor  = torch.tensor(2.)
dropout_p  = 0.789316345

# Input tensors to the model
q = torch.randn([batch_size, query_length, embedding_dim])
k = torch.randn([batch_size, key_length, embedding_dim])
v = torch.randn([batch_size, value_length, embedding_dim])
 
# Inputs to the model 
__output__  = m(q, k, v, scale_factor=scale_factor, dropout_p=dropout_p)
 

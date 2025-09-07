
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
 
        v1  = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        v2  = v1 / inv_scale_factor   # Scale the dot product by the inverse scale factor
        v3  = v2.softmax(dim=-1)    # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)  # Apply dropout to the softmax output
 
        return v4


# Initializing the model
m = Model()
 
# Inputs to the model
q1  = torch.randn(8, 256)  # Create a 2D input tensor for the query with size (batch_size, embed_dim), e.g., shape: [8x256]
k1  = torch.randn(4300, 256)   # Create another 2D input tensor for the key with size (head * batch_size, embed_dim), e.g., shape:[4300x256]
v1  = torch.randn(789200,)    # Create a 2D input tensor for the value with size (head * batch_size, sequence length), e.g., shape: [789200x300]

__outputs__  = m(q1, k1, v1)


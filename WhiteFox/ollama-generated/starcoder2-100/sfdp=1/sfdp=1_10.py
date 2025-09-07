
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):  # Inputs to the model
        scale = torch.tensor(4096).cuda().sqrt()  # Initialize a tensor for scaling factor
        inv_scale = (
            torch.tensor(32768.).cuda().inverse() 
        )  # Initialize a tensor for inverse scaling factor
 
        scaled_qk = q1 @ k1.T / scale # Compute the dot product of two tensors and scale it by the scale factor
        softmax_qk = scaled_qk.softmax(-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5) 
        output = dropout_qk @ v1.T 
        return output


# Initializing the model
m  = Model() 

# Inputs to the model
query = torch.randn(4, 8, 32768).cuda() # Initialize a query tensor of shape (batch size) × (number of heads) × (sequence length), where batch size and sequence length are arbitrary constants
key   = torch.randn(1024, 512).cuda().T # Initialize a key tensor of shape (number of heads) × (number of queries), where number of heads is an arbitrary constant
value = torch.randn(8 * query.size(-1)).view_as(key) # Initialize a value tensor of shape (batch size) × (sequence length). Batch size and sequence length are arbitrary constants
 
# Forward pass
out  = m(query, key, value)
print(out)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v2  = v1 / math.sqrt(3072) # Scale the dot product by 1/sqrt(3072)
        v3  = F.softmax(v2, dim=-1) # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.9836520274393752) # Apply dropout to the softmax output with probability of 0.9836520274393752
        v5  = v4.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return v5


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(6, 8, 3072)  # Shape is (batch size x query sequence length x embedding dimensions). For this example, the batch size and sequence lengths are equal.
key = torch.randn(6, 1536, 3072) # Shape is (batch size x key sequence length x embedding dimensions). The sequence lengths of both tensors in this example differ from each other.
value = torch.randn(48, 609, 3072) # Shape is (sequence length x batch size x embedding dimension). For this example, the batch sizes are different.

# Run the model with inputs
__output__  = m(query, key, value)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        v1  = torch.matmul(query, key) # Compute the dot product of the query and key tensors 
        scale_factor  = v1 / (v1 + 0.5 * v1).mean()  # Scale the dot product by a factor
        qk2  = v1 - scale_factor  # Subtract the scaled dot product from itself to remove the effect of scaling on softmax
        v3  = qk2.softmax(dim=-1)  
        v4  = torch.nn.functional.dropout(v3, p=0.75)  # Apply dropout to the softmax output 
        v6  = v4.matmul(value)   # Compute the dot product of the dropout output and the value tensor
        return v6


# Initializing the model
m1 = Model()
# Inputs to the model (for this example, we use query/key tensors as input tensors. But it could be any PyTorch tensor.)
query  = torch.randn(320, 784)
key   = torch.randn(320, 784)
value = torch.randn(320, 16)

# Generate a model which matches the pattern above (note that we use a different query/key pair for each output tensor)
query_gen  = torch.randn(320, 784)
key_gen   = torch.randn(320, 784)
value1  = torch.nn.functional.dropout(m1(query, key), p=0.5).matmul(torch.randn(320, 16)) # Compute the dot product of the dropout output and the value tensor
output_model_without_scalefactor  = m1(query_gen, key_gen) + torch.nn.functional.dropout(m1(query_gen, key_gen), p=0.5).matmul(torch.randn(320, 16))
value1  = value1 * 0.7 # Scale the dot product by a factor of `0.7`
output1  = m1(query, key) + torch.nn.functional.dropout(m1(query, key), p=0.5).matmul(torch.randn(320, 16)) * value1


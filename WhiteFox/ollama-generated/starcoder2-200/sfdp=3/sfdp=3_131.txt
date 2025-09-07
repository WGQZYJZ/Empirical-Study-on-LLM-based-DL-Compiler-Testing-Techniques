
class Model(torch.nn.Module):
    def __init__(self, scale=1., dropout=0., max_seq_length=8):
        super().__init__()
        self.scale  = torch.tensor([1.] * len(max_seq_length), requires_grad=False)
        self.dropout  = dropout
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v2 = v1 * self.scale.reshape(v1.size())# Scale the dot product by a factor
        v3 = scaled_qk.softmax(dim=-1)# Apply softmax to the scaled dot product
        v4 = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return v6
 


# Initializing the model with 0.5 as a scaling factor, dropout rate equal to `0`, and the maximum sequence length set to be 8.
m = Model(scale=1.,dropout=0,max_seq_length=torch.tensor([32], requires_grad=False))

# Inputs to the model with query, key, and value tensors of shape `[1, 56, 79]`, `[48, 56, 5]` and `[25, 30, 79]`, respectively.
query = torch.randn(1, max_seq_length, 56)
key   = torch.randn(1, max_seq_length, 56)
value = torch.randn(1, max_seq_length, 30)
 


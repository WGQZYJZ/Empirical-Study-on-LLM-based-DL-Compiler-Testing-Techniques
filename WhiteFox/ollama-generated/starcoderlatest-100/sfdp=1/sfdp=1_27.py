
class SelfAttention(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.q = torch.nn.Linear(embed_dim, embed_dim) # Linear layer to project queries into embedding space
        self.k = torch.nn.Linear(embed_dim, embed_dim) # Linear layer to project keys into embedding space
        self.v = torch.nn.Linear(embed_dim, embed_dim) # Linear layer to project values into embedding space
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return self.o(dropout_qk).matmul(value)
 
    def o(self, x): # Linear layer used for computing attention
        return torch.nn.functional.linear(x, self.dense1, self.activation1)\
            .transpose(-2, -1)\
            .unsqueeze(-1)\
            .repeat([1, 1, embed_dim])
 
    def linear_combine(self): # Linear layer used for combining output and input
        return torch.nn.functional.linear(x, self.dense2, self.activation2) + x
 
    def activation1(self, x): # Activation function used by o
        return torch.nn.functional.gelu(x)
    
    def activation2(self, x): # Activation function used by linear_combine
        return torch.tanh(x)

m = SelfAttention()


# Inputs to the model
query  = torch.randn(16, 3, 64, 64)
key    = torch.randn(16, 3, 64, 64)
value  = torch.randn(16, 3, 64, 64)

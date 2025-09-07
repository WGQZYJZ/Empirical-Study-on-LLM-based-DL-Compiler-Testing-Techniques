
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(32, 4096)
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query tensor and a key tensor
        v2 = v1.mul(scale_factor) # Scale the dot product by a factor
        v3  = self.attn(v2) # Apply attention using scaled dot product as query input for a linear transformation
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)# Apply dropout to the result of the previous linear layer
        v5 = v4.matmul(value) # Compute the dot product of the output of the previous dropout layer and the value tensor
        return v5


# Initializing the model
m  = Model()
 
# Inputs for the model
q1, k1, v1  = torch.randn(2048, 32), torch.randn(2048, 32), torch.randn(2048, 4) # Query is an input to the attention layer; key and value are intermediate results of the previous operations
scale_factor  =  0.5196712 ; dropout_p  =  0.1
 

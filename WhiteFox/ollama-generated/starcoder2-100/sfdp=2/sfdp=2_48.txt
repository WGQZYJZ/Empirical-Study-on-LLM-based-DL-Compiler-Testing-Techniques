
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(torch.randn(2,4)) # Initializing the query layer of the model
        self.key   = torch.nn.Parameter(torch.randn(3,5)) # Initializing the key layer of the model 
        self.value  = torch.nn.Parameter(torch.randn(10,7)) # Initializing the value layer of the model
 
    def forward(self, dropout_p=0):
        qk  = torch.matmul(query, key.transpose(-2,-1))  # Compute the dot product of the query and the key
        scaled_qk = qk / np.sqrt(3)                       # Scale the dot product by a sqrt(dimensionality of the key and value layers). 
        softmax_qk = scaled_qk.softmax(dim=-1)            # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk .matmul(value)                 # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m  = AttentionModel()

# Inputs to the model
x1 = torch.randn(2,5) 
x2 = torch.randn(3,7) 
 
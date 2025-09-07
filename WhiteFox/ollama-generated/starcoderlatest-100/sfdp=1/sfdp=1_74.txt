
class Model(torch.nn.Module):
    def __init__(self, query_shape=2048):
        super().__init__()
 
        self.query = torch.nn.Linear(query_shape, 65536)
        self.key   = torch.nn.Linear(query_shape, 65536)
        self.value = torch.nn.Linear(1024, 65536)
 
    def forward(self, query):
        query = query.unsqueeze(-1).transpose(1, 2) # Transpose the input tensor for a convolutional layer
        key   = self.key(query).transpose(0, -2) # Compute the value of the transposed key tensor
 
        qk = torch.matmul(query, key) # Compute the dot product of the query and key tensors
        scaled_qk = qk / math.sqrt(float(query.size(-1))) # Scale the dot product by sqrt(dim)
        softmax_qk = F.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=dropout_p, training=True) # Apply dropout to the softmax output
 
        output = torch.matmul(dropout_qk, self.value) # Compute the dot product of the dropout output and the value tensor
        return output.squeeze(-1).transpose(1, 2)
 
 
# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(32, 2048, 64, 64)

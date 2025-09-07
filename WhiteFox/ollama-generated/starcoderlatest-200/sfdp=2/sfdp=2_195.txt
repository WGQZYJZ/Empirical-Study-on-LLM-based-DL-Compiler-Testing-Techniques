
class Model(torch.nn.Module):
    def __init__(self, query_dim: int, key_dim: int, value_dim: int):
        super().__init__()
 
        self.query = torch.nn.Linear(query_dim, key_dim) # Initialize a weight matrix for the dot product of a query and a key as well as a bias vector
        self.key   = torch.nn.Linear(key_dim  , value_dim)
        self.scale = torch.nn.Parameter(torch.zeros(1)) # Initialize scale factor
 
    def forward(self, x1):
        query  = self.query(x1).unsqueeze(-2)  # Apply the Linear transformation to the input tensor and expand the dimensions to be the number of batches along the first dimension
        key    = self.key(x1).unsqueeze(-3)   # Apply the Linear transformation to the input tensor and expand the dimensions to be the number of batches along the third dimension
 
        qk     = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query tensor and a key tensor
        scaled_qk = qk / self.scale             # Scale the dot product by the scale factor
        softmax_qk  = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply Softmax to the output of the linear transformation to obtain attention weights
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
 
        output = dropout_qk.matmul(self.key(x1))   # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model(query_dim = 1024, key_dim = 1024, value_dim = 512)

# Inputs to the model
x1 = torch.randn(16, 3, 64, 64)

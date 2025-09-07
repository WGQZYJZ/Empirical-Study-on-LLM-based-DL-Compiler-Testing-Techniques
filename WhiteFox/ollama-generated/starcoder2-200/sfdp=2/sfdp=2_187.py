
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(16, 32) # Initialize the query to be a random tensor with shape (16, 32).
        self.key  = torch.randn(32, 10)  # Initialize the key to be a random tensor with shape (32, 10).
        self.value  = torch.randn(32, 8) # Initialize the value to be a random tensor with shape (32, 8).
 
    def forward(self):
        scale_factor  = 1e-6
        dropout_p  =  0.5
        
        v1  = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of the query and the key.
        v2  = v1 / scale_factor  # Scale the dot product by the scale factor.
        v3  = softmax(v2, dim=-1) # Apply softmax to the scaled dot product.
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) # Apply dropout to the softmax output.
        v5  = v4.matmul(value) # Compute the dot product of the dropout output and the value.
        return v5


# Initializing the model
m  = Model()
 

# Inputs to the model:

x1  = torch.randn(32, 8).float()   # Initialize x1 as a random tensor with shape (32, 8) and data type float32.
x2  = torch.randn(10, 4).float()    # Initialize x2 as a random tensor with shape (10, 4) and data type float32.

__output__  = m()


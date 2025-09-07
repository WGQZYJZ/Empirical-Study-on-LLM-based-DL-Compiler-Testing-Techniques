
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.Tensor(2, 3)) # Create a weight parameter and set its value with an initializer
        self.key   = torch.nn.Parameter(torch.Tensor(1, 4)) # Create another weight parameter and set its value with an initializer
        self.scale_factor = 0.70710678118654755  # Scale the dot product by a factor
 
        self.fc = torch.nn.Linear(5 * 5, 3) # Create a linear layer and set it's bias to zero
 
    def forward(self, x):
        # Compute the dot product of the query and key tensors
        qk = torch.matmul(x, self.query) # Matrix multiplication of input x and weight parameter
        
        # Scale the dot product by a factor
        scaled_qk = qk * self.scale_factor
        
        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(-1)
        
        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.p)
    
        # Compute the dot product of the dropout output and the value tensor
        output = dropout_qk.matmul(x)
        
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3, 4) # Shape: (batch_size, number of heads, height, width)
x2 = torch.randn(1, 1, 5, 6) # Shape: (batch_size, number of heads, depth, channels)

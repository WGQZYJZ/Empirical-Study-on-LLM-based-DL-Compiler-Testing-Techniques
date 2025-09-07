
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(256, 2048)
        self.key  = torch.nn.Linear(256, 1024)
        self.value  = torch.nn.Linear(256, 768)
        self.softmax  = torch.nn.Softmax(-1)
 
    def forward(self, query):
        vquery = self.query(query) # Apply linear transformation to the input tensor
        vkey  = self.key(vquery)   # Apply another linear transformation to the input tensor
        value = self.value(vquery) # Apply a third linear transformation to the input tensor
        
        qk  = torch.matmul(vquery, vkey.transpose(-2, -1)) # Compute the dot product of the query and key
        scaled_qk  = qk / inv_scale_factor   # Scale the dot product by an inverse scale factor
        softmax_qk  = self.softmax(scaled_qk)    # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5, training=self.training)   # Apply dropout to the softmax output
        
        output  = torch.matmul(dropout_qk, value)  # Compute the dot product of the dropout output and the value
        return vquery

# Initializing the model
m  = AttentionModel()

# Input tensors to the model
x1  = torch.randn(32, 512)   # Shape: (batch_size x num_heads * head_size)

# Initializing the optimizer and loss function
optimizer  = torch.optim.SGD(m.parameters(), lr=0.001)
loss_fn  = torch.nn.MSELoss()

# Training step
for batch in range(num_batches):
    # Forward pass
    output  = m(x1)
    
    # Compute loss on the target output and run backward to compute gradients with respect to all parameters
    loss  = loss_fn(output, target)  
    optimizer.zero_grad()  # Set grads of all tensors to zero so they can be accumulated into
    loss.backward()   # Accumulate gradient wrt each parameter
    optimizer.step()    # Take a single optimization step


# Input tensors and outputs for the model
x1 = torch.randn(32, 512)
x2 = torch.randn(64, 512)
 
__output_1__ = m(x1)[0]
__output_2__ = m(x2)[0]



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(1, 8) 
        self.key = torch.randn(32, 8)
        self.value = torch.randn(32, 64)
 
    def forward(self, query=None, key=None, value=None):
        qk = torch.matmul(query or self.query, (key or self.key).transpose(-1,-2)) # Compute the dot product of a query and key tensor 
        scaled_qk = qk * scale_factor  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output 
        output = dropout_qk @ value or self.value  # Compute the dot product of a dropout tensor and a value tensor
        return output

# Initializing the model
model = Model()
 
# Input tensors to the model
query = torch.randn(1, 8)
key = torch.randn(32, 8)
value = torch.randn(32,64)

 # Run inference with input tensors and initialize variables to compute gradients.
with torch.enable_grad():
    output = model(query=query, key=key, value=value)
 
 # Define a loss function.
loss = torch.nn.CrossEntropyLoss()
 
# Compute the backward pass. 
loss(output).backward()


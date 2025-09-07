
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 256) # Create a linear layer with input dimensions 256 and output dimensions 256
        self.key = torch.nn.Linear(256, 256) # Create a linear layer with input dimensions 256 and output dimensions 256
        self.value = torch.nn.Linear(256, 256) # Create a linear layer with input dimensions 256 and output dimensions 256
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, self.query.weight.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2) # Compute the dot product of the dropout output and the value tensor
        return output
 

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 256, dim1=50, dim2=384).div_(inv_scale_factor) # Rescale all values of the query tensor by 1/256 and divide them by a constant to avoid integer underflow
key = torch.randn(1, 256, dim1=50, dim2=384).div_(inv_scale_factor) # Rescale all values of the key tensor by 1/256 and divide them by a constant to avoid integer underflow

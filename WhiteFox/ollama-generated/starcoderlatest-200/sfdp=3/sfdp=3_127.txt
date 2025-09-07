
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8) 
        self.key = torch.nn.Linear(8, 8)
 
    def forward(self, x1, x2):
        query_tensor = self.query(x1) # Apply linear transformation to the input tensor
        key_tensor = self.key(x2)
        qk = torch.matmul(query_tensor, key_tensor.transpose(-2,-1)) * scale_factor # Compute the dot product of the query and key tensors
        softmax_qk  = nn.functional.softmax(qk)  # Apply softmax to the scaled dot product
        dropout_qk = nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, self.value(x2))  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)

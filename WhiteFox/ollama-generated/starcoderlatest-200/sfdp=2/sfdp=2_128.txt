
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(768, 3072)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / math.sqrt(128) # Scale the dot product by the inverse scale factor
        softmax_qk = F.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, x2) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(10, 3072) 
x2 = torch.randn(10, 768)

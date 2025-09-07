
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Linear(512, 32)
        self.key = torch.nn.Linear(512, 32)
        self.value = torch.nn.Linear(512, 32)
 
    def forward(self, x1):
        query = self.query(x1)
        key = self.key(x1)
        value = self.value(x1)
 
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
 
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
 
 # Inputs to the model
 x1 = torch.randn(1, 512, 3072)
 
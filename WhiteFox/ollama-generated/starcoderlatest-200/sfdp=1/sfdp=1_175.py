
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 16)
        self.key = torch.nn.Linear(8, 32)
        self.value = torch.nn.Linear(8, 64)
 
    def forward(self, qk):
        qk  = torch.matmul(self.query(qk), self.key(qk)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.value(qk)) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
qk  = torch.randn(8, 16)

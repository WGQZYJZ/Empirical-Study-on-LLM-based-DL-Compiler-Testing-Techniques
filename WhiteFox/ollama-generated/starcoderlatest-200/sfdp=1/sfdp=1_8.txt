
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 512)
        self.key = torch.nn.Linear(768, 512)
        self.value = torch.nn.Linear(768, 512)
 
    def forward(self, x):
        qk = torch.matmul(self.query(x), self.key(x).transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return dropout_qk.matmul(self.value(x)) # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 768, 32, 32)

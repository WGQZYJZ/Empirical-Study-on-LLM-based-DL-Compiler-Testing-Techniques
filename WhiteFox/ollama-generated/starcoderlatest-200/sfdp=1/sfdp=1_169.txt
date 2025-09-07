
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 128)
        self.key = torch.nn.Linear(64, 128)
        self.value = torch.nn.Linear(64, 128)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk / self.scale_factor # Scale the dot product by a scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, value) # Compute the dot product of the dropout output and the value tensor
        return output


# Inputs to the model
query = torch.randn(1, 32, 64)
key = torch.randn(1, 32, 64)
value = torch.randn(1, 32, 64)
m = Model()
output = m(query, key, value)

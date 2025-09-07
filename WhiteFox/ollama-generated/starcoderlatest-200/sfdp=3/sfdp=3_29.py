
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer = torch.nn.Linear(1, 8)
        self.key_layer = torch.nn.Linear(32, 64)
        self.value_layer = torch.nn.Linear(64, 32)
 
    def forward(self, q1):
        qk = torch.matmul(q1, self.query_layer.weight.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.value_layer.weight) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(2, 8, 64, 64)

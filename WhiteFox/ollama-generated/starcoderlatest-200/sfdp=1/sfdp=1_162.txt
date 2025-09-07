
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_heads = torch.nn.ModuleList([
            torch.nn.Linear(128, 32), # Each head has its own projection matrix
        ])
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2) # Compute the dot product of query and key tensors
        scaled_qk = qk / (key_size ** -0.5) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, x2) # Compute the dot product of the dropout output and value tensor
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, key_size, key_size)
x2 = torch.randn(1, 3, value_size, value_size)

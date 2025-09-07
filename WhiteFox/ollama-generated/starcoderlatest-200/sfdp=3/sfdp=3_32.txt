
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 1024)
        self.attention = torch.nn.MultiheadAttention(1024, 8)
 
    def forward(self, x1):
        qk = self.attention(x1, x1, x1)[0] # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = self.linear(dropout_qk) # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)

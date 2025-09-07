
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(1024, 3072)
 
    def forward(self, q1, k1, v1):
        qk = torch.matmul(q1, k1.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = self.attention(dropout_qk) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(2, 80, 3, 46) # query tensor with shape (N, M, C, HxW)
k1 = torch.randn(2, 80, 3, 46) # key tensor with shape (N, M, C, HxW)
v1 = torch.randn(2, 80, 3, 46) # value tensor with shape (N, M, C, HxW)

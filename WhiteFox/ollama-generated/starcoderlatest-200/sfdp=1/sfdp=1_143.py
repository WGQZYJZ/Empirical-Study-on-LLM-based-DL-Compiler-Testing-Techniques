
class SelfAttention(torch.nn.Module):
    def __init__(self, dim=256):
        super().__init__()
        self.linear_k = torch.nn.Linear(dim * 3, dim)
        self.linear_v = torch.nn.Linear(dim * 3, dim)
 
    def forward(self, x1, x2, x3):
        k = F.relu(self.linear_k(torch.cat((x1, x2, x3), dim=-1)))
        v = F.relu(self.linear_v(torch.cat((x1, x2, x3), dim=-1)))
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return qk, scaled_qk, softmax_qk, dropout_qk, output
 

# Initializing the model
m = SelfAttention()

 # Inputs to the model
x1 = torch.randn(256, 3, 64, 64)
x2 = torch.randn(256, 3, 64, 64)
x3 = torch.randn(256, 3, 64, 64)
__qk__, __scaled_qk__, __softmax_qk__, __dropout_qk__, output = m(x1, x2, x3)



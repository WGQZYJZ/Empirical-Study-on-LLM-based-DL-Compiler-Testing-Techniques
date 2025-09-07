
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2, x3):
        qk  = torch.matmul(x2, x3.transpose(-2, -1))  # Compute the dot product of the query and the key
        inv_scale_factor = torch.rsqrt(torch.pow(q.size(0), 0.5) * torch.pow(key.size(0), 0.5))  # Compute the inverse scale factor
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value = dropout_qk.matmul(x1)  # Compute the dot product of the dropout output and the value
        return value


# Initializing the model
m = Model()

# Inputs to the model
x1, x2, x3 = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 5, 5), torch.randn(1, 10)

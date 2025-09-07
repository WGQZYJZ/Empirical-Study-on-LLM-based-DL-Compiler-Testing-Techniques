
class SelfAttention(torch.nn.Module):
    def __init__(self, dim=3072, num_heads=4):
        super().__init__()
        self.dim  = dim
        self.num_heads  = num_heads
        self.query  = torch.nn.Linear(self.dim, self.dim * self.num_heads)
        self.key  = torch.nn.Linear(self.dim, self.dim * self.num_heads)
        self.value  = torch.nn.Linear(self.dim, self.dim * self.num_heads)
        self.scale = math.sqrt(3072 / num_heads)
        self.inv_scale = 1 / math.sqrt(3072 / num_heads)
 
    def forward(self, q):
        kq  = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk  = kq.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


m1  = SelfAttention()
# Inputs to the model
x1  = torch.randn(3072, 4)
__output__  = m1(x1)

# Initializing the model
m1 = SelfAttention()
# Inputs to the model
x1 = torch.rand(5)


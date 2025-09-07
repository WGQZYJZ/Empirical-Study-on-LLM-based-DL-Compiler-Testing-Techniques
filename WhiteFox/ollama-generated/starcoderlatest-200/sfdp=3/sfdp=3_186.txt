
class Model(torch.nn.Module):
    def __init__(self, num_queries):
        super().__init__()
        self.query = torch.nn.Linear(1024, num_queries)
 
    def forward(self, x1):
        qk  = self.query(x1).transpose(-2, -1)  # Compute the dot product of the query and key tensors
        scaled_qk = qk * scale_factor  # Scale the dot product by a factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model(num_queries)

# Inputs to the model
x1 = torch.randn(1, 1024, 56, 72).transpose(-2,-1) # (bs, qkv, h, w) -> (bs, qkv, hw)

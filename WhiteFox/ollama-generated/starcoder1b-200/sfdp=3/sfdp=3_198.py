
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_key = torch.nn.Linear(d_k, d_v)
        self.linear_query = torch.nn.Linear(d_v, d_v)
 
    def forward(self, x1):
        query = self.linear_query(x1)
        key = self.linear_key(x1)
        qkv = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qkv = qkv.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qkv = scaled_qkv.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qkv = torch.nn.functional.dropout(softmax_qkv, p=dropout_p)  # Apply dropout to the softmax output
        value = dropout_qkv.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)

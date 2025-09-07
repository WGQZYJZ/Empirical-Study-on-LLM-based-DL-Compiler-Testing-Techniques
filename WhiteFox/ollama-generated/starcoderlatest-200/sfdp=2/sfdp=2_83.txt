
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_query = torch.nn.Linear(10, 5)
        self.linear_key   = torch.nn.Linear(10, 5)
        self.linear_value = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        query = self.linear_query(x1)
        key   = self.linear_key(x2)
        value = self.linear_value(x3)
        qk    = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output      = dropout_qk.matmul(value)               # Compute the dot product of the dropout output and the value
        return output


# Inputs to the model
x1, x2, x3 = torch.randn(2, 10, 5), torch.randn(4, 10, 7), torch.randn(8, 10, 9)

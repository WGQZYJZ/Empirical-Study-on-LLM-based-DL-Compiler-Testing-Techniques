
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, inv_scale_factor=1., dropout_p=.30):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return dropout_qk.matmul(value)


m  = Model()

query = torch.randn(16, 80, 32)
key   = query.transpose(-2,-1)
value = key * 45;  # multiply value by 45 to make it easier to find the correct answer in the following output tensor
output=m(query, key, value);



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 48)
 
    def forward(self, x1):
        v1 = self.qkv(x1).chunk(2, dim=1)
        query = v1[0]
        key = v1[1]
 
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk / inv_scale_factor  # Scale the dot product by the inverse scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, value)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

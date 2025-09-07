
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk / scale_factor  # Scale the dot product by an inverse scale factor
        softmax_qk = self.softmax(scaled_qk)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)
scale_factor = 2
dropout_p = 0.3

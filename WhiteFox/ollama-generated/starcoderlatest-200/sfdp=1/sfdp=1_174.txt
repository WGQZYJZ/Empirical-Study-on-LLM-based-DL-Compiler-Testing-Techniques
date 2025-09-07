
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax_qk = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk / scale_factor  # Scale the dot product by the scale factor
        softmax_qk = self.softmax_qk(scaled_qk)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
query, key, value = torch.randn(16, 24, 32, 8), torch.randn(16, 36, 32, 8), torch.randn(16, 24, 32, 8)

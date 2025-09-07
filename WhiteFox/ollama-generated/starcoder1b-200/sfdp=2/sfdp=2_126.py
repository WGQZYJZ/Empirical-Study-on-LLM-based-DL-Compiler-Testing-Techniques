
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.key = torch.nn.Linear(hidden_size, hidden_size)  # The key is initialized randomly with a `normal` distribution.
        self.value = torch.nn.Linear(hidden_size, hidden_size)  # The value is initialized randomly with a `normal` distribution.
 
    def forward(self, x1, x2):
        query = x1  # Query: The shape of the first input tensor should be (batch_size, seq_length, hid_dim).
        key    = self.key(x2)   # Compute the dot product between the second input tensor and the weight matrix of the key layer.
        value  = self.value(x2) # Compute the dot product between the second input tensor and the weight matrix of the value layer.
        scaled_query = query.div(self.scaling_factor) # Scale the dot product between the two inputs by the inverse scaling factor.
        softmax_qk = scaled_query.softmax(dim=-1)  # Apply softmax to the scaled dot product.
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output.
        result = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value.
        return result


# Initializing the model
m = Model(hidden_size=128)
__output__  = m(x1, x2)


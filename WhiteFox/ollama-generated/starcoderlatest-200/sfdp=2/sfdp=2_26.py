
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout_key = torch.nn.Dropout(p=0.1)
 
    def forward(self, x1, x2):
        key = self.dropout_key(x2)
        qk = torch.matmul(x1, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk / (1 / math.sqrt(key.shape[-1]))  # Scale the dot product by the inverse scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        output = torch.nn.functional.dropout(input=softmax_qk, p=0.1)  # Apply dropout to the softmax output
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = x1 + 2 * x1


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key_layer = torch.nn.Linear(1024, 1024)

    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk / 2  # Scale the dot product by 2
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.key_layer(self.value))  # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()


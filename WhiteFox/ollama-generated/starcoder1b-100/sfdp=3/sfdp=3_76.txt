
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(...)  # Query embedding layer
        self.key = torch.nn.Linear(...)  # Key embedding layer
        self.value = torch.nn.Parameter(...)  # Value embedding layer
 
    def forward(self, input_tensor):
        qk = torch.matmul(input_tensor, self.query.weight)  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(self.scale)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.p)  # Apply dropout to the softmax output
        value = dropout_qk.matmul(input_tensor)  # Compute the dot product of the dropout output and the value tensor
        return self.value * value  # Return a parameterized mapping


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(...)  # Define query embedding
        self.key = torch.nn.Linear(...)  # Define key embedding
        self.value = torch.nn.Linear(...)  # Define value embedding
        self.scale_factor = 1.0  # Initialize the scale factor

    def forward(self, x):
        # Forward pass
        k = self.query(x)  # Compute the embedding from x to query
        v = self.value(x)  # Compute the embedding from x to value
        qkv = torch.matmul(k, v.transpose(-2, -1))  # Compute dot product of query and key tensors
        scaled_qkv = qkv.mul(self.scale_factor)  # Scale dot product by a factor
        softmax_qkv = scaled_qkv.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qkv = torch.nn.functional.dropout(softmax_qkv, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qkv.matmul(self.value)  # Compute dot product of the dropout output and value tensor
        return output


# Initializing the model
m = Model()


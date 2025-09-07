
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)  # Define the query linear layer
        self.key   = torch.nn.Linear(3, 8)
        self.value = torch.nn.Linear(3, 8)  # Define the value linear layer
 
    def forward(self, x1):
        v1  = self.query(x1).reshape(x1.shape[0], -1)  # Reshape to a tensor of shape `(batch_size, hidden_size)`.
        v2  = self.key(x1).reshape(x1.shape[0], x1.shape[1])  # Reshape the `query` output to a tensor of shape `(batch_size, hidden_size)` and then split it along the first dimension so that each row is a single key token.
        v3 = self.value(x1).reshape(x1.shape[0], -1)  # Reshape to a tensor of shape `(batch_size, hidden_size)`.
        output = torch.matmul(v1, v2).div(math.sqrt(float(self.key.weight.size(1)))) * math.sqrt(float(self.value.weight.size(0)))  # Compute the dot product of the query and key tensors (i.e., compute v1@v2/sqrt(key_dim)) then apply a dropout to the output.
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)


class Model(torch.nn.Module):
    def __init__(self, dim=128):
        super().__init__()
        self.dim = dim
        self.query = torch.nn.Embedding(vocab_size, dim)  # Set the embedding dimension to `dim`.
        self.key = torch.nn.Embedding(vocab_size, dim)  # Set the embedding dimension to `dim`.
        self.value = torch.nn.Linear(dim, dim)
        self.scale = torch.nn.Parameter(torch.ones(1))

    def forward(self, input_tensor):
        query = self.query(input_tensor[:, :self.dim])  # Compute the embedding for `input_tensor[:self.dim]`.
        key = self.key(input_tensor[:, self.dim:])  # Compute the embedding for `input_tensor[self.dim:]`.
        value = self.value(torch.cat((query, key), dim=1))  # The concatenation is `input_tensor[:, :self.dim] + input_tensor[:, self.dim:]`.
        scale = self.scale * math.sqrt(self.dim)  # Set the scale to `(sqrt(dim) ^ -0.5)` (i.e., `1 / sqrt(dim)`. This is a common technique used in the Transformer to ensure the dimension reduction remains correct.
        dropout_factor = torch.exp(-dropout_p * self.scale * math.log(math.e))  # Set the dropout factor to `(exp(dropout_p * scale) ^ -0.5)` (i.e., `1 / sqrt(dim)`. This is a common technique used in the Transformer to ensure the dimension reduction remains correct.
        scale_factor = torch.softmax(torch.mul(scale, dropout_factor))  # Compute the softmax scaling factor for the dot product operation.
        scaled_value = value * scale_factor  # Apply the scale and dropout to the value
        return scaled_value


# Initializing the model
m = Model()


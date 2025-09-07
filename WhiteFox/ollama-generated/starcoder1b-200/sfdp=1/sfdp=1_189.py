
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(64, 256)
        self.dropout = torch.nn.Dropout(p=0.3)
        self.ln1 = torch.nn.LayerNorm(768)
        self.ln2 = torch.nn.LayerNorm(256)
        self.linear = torch.nn.Linear(256, 2)
 
    def forward(self, x):
        # Query and Key are vectors of size (batch_size, query_length, hidden_dim).
        # Scale them with a softmax factor so that all probabilities sum to 1.
        x = self.dropout(x * torch.nn.functional.softmax(self.attn(x), dim=-1))

        # Transpose and reduce along time dimension.
        # This operation reduces the dimensionality of the inputs by one dimension,
        # making them more useful for matrix multiplication later on.
        x = x.transpose(-2, -1)  # (batch_size * query_length, hidden_dim)
        x = self.dropout(x * torch.nn.functional.softmax(self.attn(x), dim=-1))

        # Reshape to batch size x input sequence length
        x = x.contiguous().view(-1, 768)  # (batch_size * query_length, hidden_dim)
        # Perform the final linear operation using a layer normalization operation.
        x = self.ln2(x)
        # Apply a tanh nonlinearity to get the output of size [batch_size, input_sequence_length].
        x = torch.tanh(self.linear(x))

        return x

# Initializing the model
m = Model()


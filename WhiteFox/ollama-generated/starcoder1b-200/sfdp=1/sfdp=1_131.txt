
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(vocab_size, hidden_dim)  # Create a word embedding layer to use as the query layer
        self.key = torch.nn.Embedding(vocab_size, hidden_dim)  # Create a word embedding layer to use as the key layer
        self.value = torch.nn.Linear(hidden_dim, vocab_size)  # Create a linear layer to map between two tensors of shape (batch_size, seq_length, hidden_dim) and (vocab_size, hidden_dim), respectively. The output layer has `vocab_size` nodes which can be interpreted as the vocab size for this task.
        self.scale_factor = 1000000  # Create a constant inverse scale factor to avoid underflow in the dot product

    def forward(self, query, key, value):
        batch_size = query.shape[0]
        seq_length = query.shape[2]
        
        qk = torch.matmul(query, key) # Compute the dot product of the query and key tensors
        scaled_qk = qk / self.scale_factor # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        
        return output


# Initializing the model
m = Model()



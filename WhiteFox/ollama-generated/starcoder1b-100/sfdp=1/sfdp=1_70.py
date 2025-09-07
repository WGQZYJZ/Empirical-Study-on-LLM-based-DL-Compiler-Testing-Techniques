
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(num_embeddings, embedding_dim)  # Create an embedding for each input token
        self.key = torch.nn.Embedding(num_embeddings, embedding_dim)  # Create an embedding for each key token
        self.value = torch.nn.Parameter(torch.Tensor(embedding_dim))  # Create a random value tensor with shape (batch_size, embedding_dim)

    def forward(self, x1):
        batch_size = x1.shape[0]
        dim = x1.shape[-2:]
        x2 = self.query(x1).reshape(-1, *dim)  # Reshape the input tokens as a tensor of shape (batch_size, seq_len, embedding_dim)
        x3 = self.key(x1).reshape(-1, *dim)  # Reshape the key tokens as a tensor of shape (batch_size, seq_len, embedding_dim)
        self.value.data.fill_(0)  # Fill the value parameter with zeros
        scale_factor = self.value.shape[0] / batch_size  # Scale the dot product by the inverse of the total number of tokens in the input sequence
        key_norm = F.embedding_norm(x3, dim)  # Compute the norm of the embedding for each token
        query_norm = F.embedding_norm(x2, dim)  # Compute the norm of the embedding for each token
        scaled_qk = query_norm.div_(query_norm.abs().sqrt() + 1e-8).unsqueeze(-1)  # Scale by L<sup>2</sup>, then add 1 to prevent divide-by-zero errors, and convert it into a tensor of shape (batch_size, seq_len, 1)
        softmax_qk = scaled_qk.softmax(dim=-1).contiguous()  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v = dropout_qk.matmul(self.value)  # Compute the dot product of the dropout output and the value tensor
        return v


# Initializing the model
m = Model()

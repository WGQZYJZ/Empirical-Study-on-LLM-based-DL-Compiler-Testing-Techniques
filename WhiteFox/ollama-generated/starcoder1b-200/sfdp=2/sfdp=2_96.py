
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(vocab_size, hidden_dim)
        self.key = torch.nn.Embedding(vocab_size, hidden_dim)
        self.value = torch.nn.Embedding(vocab_size, hidden_dim)

        self.dropout_p = 0.1
 
    def forward(self, x, y):
        qk = self.query(x).matmul(self.key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        v = self.value(y).matmul(dropout_qk)  # Compute the dot product of the dropout output and the value

        return v


# Initializing the model
m = Model()



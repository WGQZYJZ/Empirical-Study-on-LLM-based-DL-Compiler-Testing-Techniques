
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(5, 3)  # Embedding matrix for the input embedding
        self.key   = torch.nn.Embedding(5, 4)
        self.value = torch.nn.Embedding(5, 4)

        self.scale_factor = 1 / math.sqrt(self.query.weight.shape[0])
        # The dot product of the query and key tensors is computed, then softmax is applied, then dropout is applied

    def forward(self, x1, x2):
        qk   = torch.matmul(x1, self.key)  # Compute the dot product of the query and key tensors
        scaled_qk = qk / (self.scale_factor * math.sqrt(self.query.weight.shape[0]))
        softmax_qk = scaled_qk.softmax(-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v = dropout_qk.matmul(self.value)  # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m = Model()



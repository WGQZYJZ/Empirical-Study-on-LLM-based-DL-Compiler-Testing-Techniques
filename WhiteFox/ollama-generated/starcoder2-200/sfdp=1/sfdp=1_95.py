
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # These constants should be 8, not 1024. The number comes from the code example: https://pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html
        self._embed_size = 64
        self.linear_out = torch.nn.Linear(self._embed_size * 3, self._embed_size)
        self.dropout = torch.nn.Dropout(0.1)
 
    def forward(self, query):
        query = query / (query.shape[-1] ** 0.5)
        kq = torch.matmul(query, query.transpose(-2, -1)) # Compute the dot product of the query and key tensors. The output is not scaled by an inverse scale factor in this model.
        scaled_qk = qk.div(self._embed_size ** 0.5) # Scale the dot product by the square root of the embedding size to prevent overflow errors with small input sizes
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)  # Apply dropout to the softmax output
        output  = self.linear_out(dropout_qk * query) # Compute the dot product of the dropout output and the value tensor
 
        return self.dropout(output), kq

# Initializing the model
am  = AttentionModel()




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(d_model, d_k)
        self.dropout1 = torch.nn.Dropout(p=dropout_p)
        self.linear2 = torch.nn.Linear(d_k, n_head * d_v)
        self.drop2 = torch.nn.Dropout(p=dropout_p)

    def forward(self, query, key):
        # Compute the dot product of the query and key tensors. The output will be a matrix with shape [batch size, sequence length, d_k].
        # Scale by an inverse of the square root of the dimension.
        # Apply softmax to the scaled dot product.
        # Use dropout after applying softmax.
        batch_size = query.shape[0]  # batch size
        seq_len = query.shape[1]
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.d_k)
        scaled_qk = qk.div(math.sqrt(self.d_k))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        # Shape: [batch size, sequence length, n head * d_v]
        return output

# Initializing the model
m = Model()



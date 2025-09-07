
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v, embed_dim=100):
        super().__init__()
        self.w_q = torch.nn.Parameter(torch.randn((d_k, embed_dim))))  # Parameter for query weights
        self.w_k = torch.nn.Parameter(torch.randn((d_v, embed_dim)))  # Parameter for key weights
        self.w_v = torch.nn.Parameter(torch.randn((embed_dim, d_v)))  # Parameter for value weights
        self.dropout = torch.nn.Dropout(p=dropout)
 
    def forward(self, x1, x2):
        # Compute the dot product of the query and the key
        qk = torch.matmul(x1, self.w_q)  # Shape: batch_size x embed_dim
        scaled_qk = qk / math.sqrt(math.floor((self.w_v).shape[0]))  # Shape: batch_size x embed_dim
        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(dim=-1)  # Shape: batch_size x embed_dim
        dropout_qk = self.dropout(softmax_qk, p=self.p)  # Shape: batch_size x embed_dim
        # Compute the dot product of the dropout output and the value
        out = dropout_qk.matmul(x2)  # Shape: batch_size x embed_dim
        return out


# Initializing the model
m = Model()


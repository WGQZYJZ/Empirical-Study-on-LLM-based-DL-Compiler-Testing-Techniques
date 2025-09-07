
class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_hops=2)
 
    def forward(self, x1, x2):
        vq  = self.attention(x1, x2, x2)[0] # Compute the dot product of the query and key tensors
        # vq is now (batch_size, query_len, query_len, num_heads), qk = vq[:, :query_len, :, :]
        # scale_factor = 1 / sqrt(num_heads)
        # output = dropout_qk.matmul(vq)  # Compute the dot product of the dropout output and the value tensor
        output = self.attention(x1, x2, qk=vq)[0]  # Compute the dot product of the query and key tensors
        return output


# Initializing the model
m = Model()



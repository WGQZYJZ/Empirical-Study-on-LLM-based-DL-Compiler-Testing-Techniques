
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(256, 256)
 
    def forward(self, q1, k1):
        v1 = self.matmul(q1)
        scaled_qk = v1
        softmax_qk = scaled_qk
        dropout_qk = softmax_qk
        output = dropout_qk @ k1.transpose(-2, -1) # The dimension of the softmax dim is 3, which means that the input tensor should be a batch matrix whose first axis is in order of the length of each example. In particular, qk has shape (L, N, M), where L and N are lengths of query sequence and key sequence, respectively, and M is dimension of embedding vector.
        return output


# Initializing the model
m = Model()

query = torch.randn(4, 256)
key   = torch.randn(3, 256) # The dimension of qk has shape (L, N, M), where L and N are lengths of query sequence and key sequence, respectively, and M is dimension of embedding vector. In particular, qk has shape (L, N, M), where L and N are lengths of query sequence and key sequence, respectively, and M is dimension of embedding vector.

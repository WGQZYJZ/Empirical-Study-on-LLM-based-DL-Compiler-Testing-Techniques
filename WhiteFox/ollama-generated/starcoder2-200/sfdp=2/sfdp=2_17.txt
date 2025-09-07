
class Model(torch.nn.Module):
    def __init__(self, embdim=768):
        super().__init__()

        self.scale = 1 / np.sqrt(2 * embdim) # Scale parameter. In practice, this value is often fixed to `1/√(d)` where d is the dimension of the embedding vector.
        self.dropout_p  = 0.1 # Probability of dropout

        self.query = torch.nn.Linear(embdim // 2, embdim)
        self.key = torch.nn.Linear(embdim // 2, embdim)
        self.value = torch.nn.Linear(embdim // 2, embdim)

    def forward(self, query):

        v1  = self.query(query) # Query embedding layer
        v2  = self.key(query) # Key embedding layer
        v3  = self.value(query) # Value embedding layer
        qk  = torch.matmul(v1, v2.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk  = qk.div(self.scale)# Scale the dot product by the scale parameter
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(v3) # Compute the dot product of the dropout output and the value

        return v1 + output, v2, qk


# Initializing the model
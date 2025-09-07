
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(vocab_size, embedding_dim)
        self.key = torch.nn.Embedding(vocab_size, embedding_dim)
 
    def forward(self, x1, x2):
        # compute query, key and value
        k  = self.key(x2)  # x2 is the context
        v  = self.value(x2)  # x2 is the context
        q  = self.query(x1)  # x1 is the query

        scaled_qk  = torch.matmul(q, k).div(math.sqrt(embedding_dim))  # compute scaled dot product by inverse sqrt(embedding_dim)
        softmax_qk = scaled_qk.softmax(-2)  # apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

        output = torch.matmul(dropout_qk, v)  # compute dot product of the context and the value

        return output


# Initializing the model
m  = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query):
        qk  = torch.matmul(query, key) # Compute the dot product of the query and the key
        scaled_qk  = qk * 0.7071067811865476
        softmax_qk  = scaled_qk.softmax(-2)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax, p=0.3) # Apply dropout to the softmax output
        output  = dropout_qk @ value1
        return v6


# Initializing the model and feeding inputs into it
m  = Model()
x2  = torch.randn(1, query_dim)
__output___  = m(x2)


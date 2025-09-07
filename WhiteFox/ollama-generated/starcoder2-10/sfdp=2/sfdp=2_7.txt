
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v1  = torch.matmul(query1, key2.transpose(-2, -1))
        v2  = v1 / float(50) 
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=float(79)/100.) # Dropout with probability of `p=0.8` (in percentage)
        v6  = value3.matmul(v4)
        return v6

# Initializing the model
m  = Model()

# Inputs to the model
query1  = torch.randn(5, 9728, 768) # Query of size (batch_size x sequence_length x embedding_dimensionality)
key2  = torch.randn(5, 9728, 768) # Key of size (batch_size x sequence_length x embedding_dimensionality)
value3 = torch.randn(5, 9728, 1024) # Value of size (batch_size x sequence_length x hidden_dimensionality)


__output__  = m(query1, key2, value3)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None):
        qk = torch.matmul(query, key.transpose(-2,-1)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result 
        attn_weight = torch.dropout(attn_weight, dropout_p=0.5, train=self.training)  # Apply dropout to the softmax output
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return v6


# Initializing the model
m  = Model()


# Inputs to the model
query = torch.randn(4,128)  # Input data for query
key   = torch.randn(30000*4, 128)  # Input data for key, it should be generated based on `torch.randint` with input size (30000*4, 128), because the length of key is not fixed


# Initializing the model instance
m = Model()
m(query, key)
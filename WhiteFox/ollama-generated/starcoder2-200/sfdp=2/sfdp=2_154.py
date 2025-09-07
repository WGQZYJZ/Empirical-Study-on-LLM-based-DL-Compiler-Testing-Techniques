
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of a query and a key 
        v2 = v1 / 507369.4348104
        v3 = torch.nn.functional.softmax(v2, dim=-1) # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=0.1) # Apply dropout to the softmax output 
        return  v4 @ value


# Initializing the model with a fixed random seed
m  = Model()
torch.manual_seed(0)

# Inputs to the model - query and key are randomly generated with the same shape. The value is also randomly generated but has the same shape as the query. 
query = torch.randn(1,32,768//4).to('cuda')
key = torch.randn(1,32,768//4) .to('cuda') # Shape: (batch_size, sequence length, embedding dimension)
value = torch.randn(1, 5, 768)



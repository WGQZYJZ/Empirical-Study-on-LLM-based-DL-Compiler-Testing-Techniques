
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(784, 256)
        self.dropout1 = torch.nn.Dropout(0.5)
 
    def forward(self, x1):
        # Compute dot product and attention weights of queries and keys for each head
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
    
        # Compute a weighted sum of the values using the attention weights 
        output = attention_weights.matmul(value)
    
    return v6

# Initializing the model 
m = Model()


# Inputs to the model
x2 = torch.randn(batchsize, 784)

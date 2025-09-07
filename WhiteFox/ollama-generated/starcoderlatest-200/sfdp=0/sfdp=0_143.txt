
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Apply the scaling factor to the dot product
        attention_weights = F.softmax(scaled_dot_product, dim=-1)  # Use softmax operation on the scaled dot product matrix
        output = attention_weights.matmul(value)  # Compute a weighted sum of values using the weights from the previous step and value tensor
        return output
 

# Initializing the model
m = Model()
 
# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / math.sqrt(query.size()[-1])
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
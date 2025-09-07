
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
       scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d)
         attention_weights = scaled_dot_product.softmax(dim=-1)
            return  attention_weights.matmul(value)


# Initializing the model and inputs to it

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)

        attention_weights = scaled_dot_product.softmax(dim=-1) # softmax to make sure the sum is 1 over dim - 1
        
        output = attention_weights.matmul(value)
        return output


# Initializing the model
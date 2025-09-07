
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tensor:
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(torch.tensor(key).shape[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        output  = attention_weights.matmul(value)
        return output

# Initializing the model
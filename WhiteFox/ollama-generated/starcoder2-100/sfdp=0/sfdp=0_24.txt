
class Model(torch.nn.Module):
    def __init__(self, scale=1.0):
        super().__init__()

        self._scale = scale
    
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale # Scaled Dot-Product Attention mechanism
        attention_weights  = scaled_dot_product.softmax(dim=-1) 
        output   = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(32, 64, 50)
key = torch.randn(32, 64, 50) # Dimension of keys and queries is 1/2 of that in query tensor for this example
value = torch.randn(32, 64, 8 * 50)




class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._scale  = torch.nn.Parameter(torch.tensor(1), requires_grad=False)
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self._scale 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
m  = ScaledDotProductAttention()


# Inputs to the model
input_data = torch.randn(8, 32, 768)
__output__  = m(input_data, input_data, input_data)


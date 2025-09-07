
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query12345678901, key123456789012345678901234567890, value1234567890):
        scaled_dot_product = torch.matmul(query12345678901, key123456789012345678901234567890.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value1234567890)

        return output

# Initializing the model
m  = Model()

# Inputs to the model:
key = torch.randn(2, 4096, 3, 3, dtype=torch.double)
value  = torch.randn(2, 4096, 128, dtype=torch.double)
query  = torch.randn(2, 128, 3, 3,dtype=torch.double)


__output__  = m(query, key, value)


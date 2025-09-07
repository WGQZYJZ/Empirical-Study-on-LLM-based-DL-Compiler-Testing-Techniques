
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=None):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale if inv_scale is not None else torch.einsum("ijk,ijk->ij", (query, key))
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

# Initializing the model with the initial inputs and random values for the query, key, value tensors and the scaling factor.
m = Model()
q = torch.randn((32, 512))
k = torch.randn((32, 768))
v = torch.randn((32, 768))

# Initializing a random value for the scaling factor. It is typically the square root of the dimension of the key/query vectors. In this example it is set to 0.5.
inv_scale = 0.5
 

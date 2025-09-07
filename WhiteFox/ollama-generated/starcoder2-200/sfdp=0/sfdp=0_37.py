
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        inv_scale = torch.sqrt(key[0].shape[-1])
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        output = attention_weights.matmul(value)
 
        return output


# Initializing the model
m  = Model()


# Inputs to the model
qry  = torch.randn(8, 4096)
key  = torch.randn(256, 4096)
val  = torch.randn(32768, 16, 16)


# Running the model with different inputs each time

for i in range(10):
    __output__  = m(qry, key, val)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

# Initializing the model
m = Model()


# Inputs to the model (Note that inv_scale is not defined as a constant in the previous version)
query  = torch.randn(32, 64, 1024)
key = torch.randn(32, 64, 1024)
value  = torch.randn(32, 64, 1024)

 # Initializing the model (Note that inv_scale is not defined as a constant in the previous version)
m  = Model()


# Inputs to the model 
query  = torch.randn(32, 64, 1024)
key = torch.randn(32, 64, 1024)
value  = torch.randn(32, 64, 1024)

# Initializing the model (Note that inv_scale is not defined as a constant in the previous version)
m  = Model()

 # Inputs to the model
query  = torch.randn(32, 64, 1024)
key = torch.randn(32, 64, 1024)
value  = torch.randn(32, 64, 1024)

 # Initializing the model (Note that inv_scale is not defined as a constant in the previous version)
m  = Model()


class Model(torch.nn.Module):
    def __init__(self, dim=160, scale=4, bias="cls"):
        super().__init__()
 
        self.scale = torch.nn.Parameter(
            data=torch.full((dim,), fill_value=(2/scale)), 
            requires_grad=True)
 
        if isinstance(bias, str):  # cls or mean
            self.bias = nn.Parameter(
                data=torch.zeros((1, dim), dtype=torch.float32))
        else:
            self.register_buffer("bias", bias)
 
    def forward(self, qk):

        query = qk[:, :self.scale] # 48
        key   = qk[:, -self.scale:] / self.scale
 
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(qk).add(self.bias) # 48
        return output


# Initializing the model
m  = Model()

# Inputs to the model
query_tensor = torch.randn(256, 960) / 1000000
key_tensor   = torch.randn(256, 480) / 1000000


# Initializing the model
m  = Model()

# Inputs to the model
query_tensor = torch.randn(256, 960) / 1000000
key_tensor   = torch.randn(256, 480) / 1000000



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.randn(512) / 8 # random key/query vector (in this case, a scalar value)
        self.value = torch.randn(37906) # random value tensor
        self.scale = math.sqrt(self.key.shape[0])
 
    def forward(self):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        return attention_weights.matmul(value)


# Initializing the model
m  = Model()


class Model(torch.nn.Module):
    def __init__(self, inv_scale = 1024):
        super().__init__()
 
        self.inv_scale = inv_scale
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size()[-1]) 
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)

        return output

# Initializing the model with custom scaling factor
inv_scale  = torch.randint(low=5, high=2048*3) + torch.randint(low=5, high=2048)*1e-6
m  = Model(int(torch.Tensor([float(i)])[0]))

# Input tensors to the model with shape (batch_size x num_queries x  key/query dimensionality) and (batch size x num_keys x value dimensionality), respectively.
x1, x2, x3 = torch.randn(8, 512*4096*2, 768//2 ), torch.randn(8, 512*4096, 768//2 ), torch.randn(batch_size, num_queries, key/query dimensionality)

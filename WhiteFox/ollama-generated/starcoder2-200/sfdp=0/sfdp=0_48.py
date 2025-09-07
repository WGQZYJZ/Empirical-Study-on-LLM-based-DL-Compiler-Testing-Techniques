
class Model(torch.nn.Module):
    def __init__(self, inv_scale = 2048.0):
        super().__init__()
 
        self.query = torch.randn([32,65536])
        self.key   = torch.randn([192,65536]) * inv_scale + 1e-9

        self.scale = float(self.key)
 
    def forward(self):
        scaled_dot_product = torch.matmul(query, key.transpose(-2,-1)) / scale
        attention_weights   = scaled_dot_product.softmax(dim=-1)
 
        return attention_weights

# Initializing the model
m  = Model()
__output___ = m()


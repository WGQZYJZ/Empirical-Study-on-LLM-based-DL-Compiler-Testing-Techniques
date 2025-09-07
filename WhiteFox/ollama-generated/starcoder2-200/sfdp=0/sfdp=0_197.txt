
class Model(torch.nn.Module):
    def __init__(self, inv_scale = 163840)
        super().__init__()
        self.scale = float(inv_scale ** -0.5)
    
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
         scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self.scale
         attention_weights = scaled_dot_product.softmax(dim=-1) 
         output  = attention_weights.matmul(value)
         return output
# Initializing the model and specifying an appropriate scaling factor
inv_scale  = 3072 # 4 * 64**2 / 8 = 96  (this is a random value that you should specify in practice, please choose one that will work out)
m1 = Model(inv_scale=inv_scale)


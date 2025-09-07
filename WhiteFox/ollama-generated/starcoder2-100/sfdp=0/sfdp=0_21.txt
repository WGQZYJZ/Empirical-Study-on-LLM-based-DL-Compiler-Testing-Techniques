
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.randn([32768, 1], dtype=torch.float)
        self.value = torch.randn([4096, 32768], dtype=torch.float)
        self.query = torch.randn([512, 4096], dtype=torch.float)
 
    def forward(self):
        inv_scale  = ((self.key.shape[-1] ** -0.5).expand(-1,-1))
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

# Initializing the model and setting fixed seeds for randomness control
m  = Model()
 
# Setting fixed seed to 42 for reproducibility of results, etc...
torch.manual_seed(42)


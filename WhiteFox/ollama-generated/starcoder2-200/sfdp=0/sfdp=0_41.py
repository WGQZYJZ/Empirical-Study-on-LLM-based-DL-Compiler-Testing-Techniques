
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._inv_scale  = torch.tensor([512.], dtype=torch.float32)
 
    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor):
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / self._inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output             = attention_weights.matmul(v)
# Initializing the model
m  = MyModel()

 # Inputs to the model
 query   = torch.randn([3, 64])
 key     = torch.randn([3, 800, 512])
 value   = torch.randn([3, 800, 512])
 
 # Passing inputs through model

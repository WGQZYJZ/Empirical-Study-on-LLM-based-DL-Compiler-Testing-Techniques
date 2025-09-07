
class Attention(torch.nn.Module):
    def __init__(self, d_k: int, d_v: int, d_model: int, scale: bool = False):
        super().__init__()
        self.scale = scale
 
        self.d_k = d_k
        self.d_v = d_v
        self.d_model = d_model
 
        if self.scale:
            self.scale_factor = (self.d_k ** -0.5)
 
    def forward(self, query, key, value, scale=False):
 
        # Query, Key and Value are supposed to be already transposed.
 
         

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale):
        super().__init__()
        self.scale = 1 / np.sqrt(inv_scale)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor,) -> Tuple[torch.Tensor]:
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) * self.scale 
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        output =  torch.bmm(attention_weights, value) 
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.sdpa = ScaledDotProductAttention(500)

    def forward(self, x1: torch.Tensor,) -> Tuple[torch.Tensor]:
        v1  = torch.randn([32, 64, 98]) 
        v2  = torch.randn([32, 70, 98]) 
        v3  = self.sdpa(v1, v2, v2) 
        return v3 

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn([32, 64, 70])
__output__  = m(x1)


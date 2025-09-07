
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
        self.layernorm1  = torch.nn.LayerNorm([7, 32])
        self.layernorm2  = torch.nn.LayerNorm([640, 512])
 
    def forward(self, q_in):
        k, v  = q_in, q_in
        scaled_dot_product  = torch.matmul(q_in, k.transpose(-2, -1)) / math.sqrt(k.shape[-1]) # scaling_factor
        attention_weights  = scaled_dot_product.softmax(dim=-1) 
        contextualized  = torch.matmul(attention_weights, v)
        combined_tensor  = self.layernorm1(contextualized + q_in)
        combined_tensor2  = self.layernorm2(combined_tensor)
 
        return combined_tensor


# Initializing the model
m  = Model()

# Inputs to the model
q_in  = torch.randn([7, 32]) # Q is batch size * query depth
__output__  = m(q_in)


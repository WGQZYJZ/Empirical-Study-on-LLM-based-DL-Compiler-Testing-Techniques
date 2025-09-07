
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=16)
 
    def forward(self, x1, x2, inv_scale):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / (inv_scale ** 0.5)
        attention_weights = self.attn(query=x1, key=x2, value=x2)[0]
        output = attention_weights * scaled_dot_product.matmul(x2)
        return output


# Initializing the model
m = Model()

 # Inputs to the model
inv_scale = torch.tensor([5e-12], requires_grad=True, device='cuda')
x1 = torch.randn(1, 16, 32, 32)
x2 = torch.randn(1, 16, 32, 32)

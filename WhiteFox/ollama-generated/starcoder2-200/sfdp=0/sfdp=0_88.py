
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.randn([2048], requires_grad=True) # 256 is good
        self.k = torch.randn([1, 768])

    def forward(self, x):
        inv_scale  = math.sqrt(x.size(-1))

        dotproduct_input  = torch.bmm(
            self.q[:, None].transpose(-2,-1), # This is the query tensor, which has shape [B, M]
            self.k.transpose(-2,-1).expand(len(self.q), x.size(0)) # This is the key tensor of the attention mechanism, which has shape [M, B]
        )
        scaled_dot_product = dotproduct_input / inv_scale

        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = torch.matmul(attention_weights[:, None], x).squeeze() # squeeze is a good practice here to avoid having extra dimensions in the output tensor and make it simpler for our analyzers.
        return output

# Initializing the model
m  = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax()
 
    def forward(self, query, key, value, inv_scale=1e-6):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale # [N]
        attention_weights  = self.softmax(scaled_dot_product)                      # [N]
        output  = attention_weights.matmul(value)                                  # [N]
        return output


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn([10, 512])            # [N, K], query vector
key    = torch.randn([4736, 512]).t()      # [K, N] or [N, K] 
value  = torch.randn([4736, 512])          # [N, V] or [V, N], value vector


__output__  = m(query, key, value)
__output__  = m(query, key[:, :, None].repeat_interleave(value.shape[-1]), value)
__output__  = m(torch.randn([4736, 512]).t(), torch.randn([839040, 512]),  value)


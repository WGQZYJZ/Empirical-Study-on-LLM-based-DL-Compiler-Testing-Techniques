
class Model(torch.nn.Module):
    def __init__(self, inv_scale=0.567128439593):
        super().__init__()

    def forward(self, q, k, v):
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.shape[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(v)
        return output


# Initializing the model
m  = Model()


__output__  = m(__input__)


class Attention(torch.nn.Module):
    def __init__(self, dim: int):
        super().__init__()
 
        self.dim  = torch.Tensor([dim]).to('cpu').long()
        # The scale factor `inv_scale` is typically the square root of the dimension of the key/query vectors, which helps to stabilize the gradients especially when the dimensions are large.
        self.inv_scale  = (self.dim ** -0.5).to(dtype=torch.float)
 
    def forward(self, query: torch.Tensor,
                key:   torch.Tensor,
                value: torch.Tensor):
 
        scaled_dot_product  = torch.matmul(query / self.inv_scale,
                                           key.transpose(-2, -1))
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output              = (attention_weights).matmul(value)

        return output


# Initializing the model with dimension of query/key/value tensor as 8
model = Attention(dim=8)
__input1__ = torch.randn([2, 5, 64]) # Input tensors to the model for query/key/value tensors: [batch_size, num_words, dim]
__input2__ = torch.randn([2, 7, 32]).to(dtype=torch.float)
__input3__ = torch.randn([2, 5, 4096])

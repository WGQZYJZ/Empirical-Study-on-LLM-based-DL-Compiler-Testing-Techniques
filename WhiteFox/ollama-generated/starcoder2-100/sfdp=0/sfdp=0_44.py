
class DotAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, qry, key, value, inv_scale=None):
        scaled_dot_product  = torch.matmul(qry, key.transpose(-2, -1)) / inv_scale if (inv_scale is not None) else torch.einsum("ijk->jki", qry @ key.transpose(-2, -1)).softmax(dim=-1)
        attention_weights  = scaled_dot_product
        output  = attention_weights.matmul(value)

        return output

# Initializing the model
model  = DotAttention()

 # Inputs to the model
qry  = torch.randn((32, 8, 64))
key  = torch.randn((32, 8, 1024))
value  = torch.randn(32, 8, 1024)

 # Initializing the model's parameters for scaling factor `inv_scale` using Xavier initializer

model  .apply(lambda m: nn.init.xavier_uniform_(m.weight))
 

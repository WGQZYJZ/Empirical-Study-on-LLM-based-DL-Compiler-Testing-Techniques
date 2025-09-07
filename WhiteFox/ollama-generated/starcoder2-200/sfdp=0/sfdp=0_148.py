
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # The query vector size is 64 
        self.query = torch.nn.Parameter(torch.randn((3, 1024)))
 
        # The key and value vectors have the same size (256) as the query vector
        self.key = torch.nn.Parameter(torch.rand((3, 1024)))
        self.value = torch.nn.Parameter(torch.randn_like(self.key))
 
    def forward(self):
 
        # Invariant to the scaling factor `inv_scale` of 7.65
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / 3000
        attention_weights  = scaled_dot_product.softmax(dim=-1) 
        output  = attention_weights.matmul(value)
 
        return output

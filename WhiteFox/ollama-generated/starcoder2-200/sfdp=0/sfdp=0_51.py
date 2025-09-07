
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, d_model=768, inv_scale=4):
        super().__init__()
        self.scale = math.sqrt(inv_scale)
 
        self.query  = torch.nn.Linear(d_model // 2, d_model) # Half the model dimension as queries
        self.key    = torch.nn.Linear(d_model // 2, d_model) 
        self.value  = torch.nn.Linear(d_model // 2, d_model)
 
        self._reset_parameters()
 
    def _reset_parameters(self):
        nn.init.normal_(self.query.weight, std=0.1) # Initialize the query layer to a normal distribution with standard deviation 0.1
        nn.init.constant_(self.key.bias, 0.)          # Set the bias of the key layer to zero 
        nn.init.constant_(self.value.bias, 0.)        # Set the bias of the value layer to zero
 
        nn.init.normal_(self.query.weight, std=0.1)
        nn.init.constant_(self.key.bias, 0.)
        nn.init.constant_(self.value.bias, 0.)
 
    def forward(self, query, key):
        scaled_dot_product = torch.matmul(
            self.scale * query, 
            key.transpose(-2, -1))
 
        attention_weights  = scaled_dot_product.softmax(dim=-1) # Softmax of the scaled dot product of the queries and keys
 
v1  = m(x1)
v2  = v3[1][0] + v4[2][0]
return v1 * v2


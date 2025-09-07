
class SelfAttentionLayer(torch.nn.Module):
    def __init__(self, dim=768, dropout: float = 0.1, inv_scale = torch.tensor(32)):
        super().__init__()
        self.linear_query  = torch.nn.Linear(dim // 4, dim) # divide dim by 4 for the query, key and value matrices.
        self.linear_key    = torch.nn.Linear(dim // 4, dim)
        self.linear_value  = torch.nn.Linear(dim // 4, dim)
        self.dropout       = torch.nn.Dropout(p=dropout)
        self.norm          = torch.nn.LayerNorm(normalized_shape=(dim))
 
        self.scaled_dot_product  = torch.nn.Linear(2 * dim, dim) # Scaled dot product is applied to compute the attention weights.
        self.inv_scale           = inv_scale
 
    def forward(self, input):
        query        = self.linear_query(input).reshape(-1, input.shape[-3], -1)  # Convert the input tensor into a 2-dimensional tensor. The first dimension is considered batch size.
        key          = self.linear_key(query).transpose(-2, -1)   # Transpose to convert the key/value tensors into a 3-dimensional tensor for dot product calculation.
        value        = self.linear_value(input).reshape(-1, input.shape[-3], -1)
 
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(self.inv_scale) # Apply the scaling factor and compute the attention weights as a softmax.
        attention_weights   = scaled_dot_product.softmax(dim=-1)
        output             = self.dropout(torch.bmm(attention_weights, value).view(-1, input.shape[-3], dim))  # BMM is used to compute the weighted sum of the value tensor.
        
        return self.norm(output)


# Initializing the model
s = SelfAttentionLayer()
 
# Inputs to the model
i = torch.randn((2, 768))
 
__output__  = s(i)

class Attention(torch.nn.Module):
    def __init__(self, querys: torch.Tensor, keys: torch.Tensor, attn_mask: torch.Tensor, dropout=0.1):
        super().__init__()
 
        self._query  = querys
        self._key  = keys
 
        # Define the attention mask
        self._attn_mask  = attn_mask
 

        self._dropout = torch.nn.Dropout(p=dropout)
 
    def forward(self, values: torch.Tensor):
        # Compute the dot product of the query and key (plus an attention mask)
        scale = math.sqrt(torch.Size(self._query.size(-1)))  # Use sqrt() to calculate the scaling factor

        # Get the number of dimensions in the input tensors
        dim_query, dim_key, dim_value = self._query.ndim, self._key.ndim, values.ndim
        # Ensure that all tensors have the same shape by padding with zeros
        if len(self._query.shape) != 3:
            self._query = torch.unsqueeze(self._query, -2).expand(-1, dim_value, -1)
        if len(self._key.shape) != 3:
            self._key = torch.unsqueeze(self._key, -2).expand(-1, dim_value, -1)
        # Compute the scaled dot product of query and key (plus attention mask)
        # First expand the attn mask to match the shape of the values.
        attn_mask  = self._attn_mask.expand(dim_query, 1, dim_key).contiguous()
        
        scale = torch.Size([self._query.size(-2)])  # Use sqrt() to calculate the scaling factor

        # Get the number of dimensions in the input tensors
        dim_query, dim_key, dim_value = self._query.ndim, self._key.ndim, values.ndim
        # Ensure that all tensors have the same shape by padding with zeros
        if len(self._query.shape) != 3:
            self._query = torch.unsqueeze(self._query, -2).expand(-1, dim_value, -1)
        if len(self._key.shape) != 3:
            self._key = torch.unsqueeze(self._key, -2).expand(-1, dim_value, -1)
        # Compute the scaled dot product of query and key (plus attention mask)
        # First expand the attn mask to match the shape of the values.
        attn_mask  = self._attn_mask.expand(dim_query, 1, dim_key).contiguous()

        scaled_dot_product = torch.matmul(self._query/scale,
                                          self._key.transpose(-2,-1))  # Compute dot product using matmul
        qkv_combined  = torch.cat([self._query , self._key] , -1)  # Concatenate the three tensors together
        attn_mask  = torch.triu(torch.ones((qkv_combined.size(-2), qkv_combined.size(-1))), diagonal=1).bool() 
        scaled_dot_product[attn_mask] = float('-inf')  # Set the attention mask to -Inf

        attn_weight = F.softmax(scaled_dot_product, dim=-1)  # Apply softmax
        attn_weight  = self._dropout(attn_weight)
        
        output = torch.matmul(attn_weight, values)  # Compute the dot product of attention weight and value
        
        return output

attn = Attention(querys=torch.randn(32,512),
                keys=torch.randn(32,512),
                attn_mask=torch.ones((32,800)))

# Initializing the model with random query tensor 
x1  = torch.randn(32 ,4)
__output__  = attn(x1)


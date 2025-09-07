
class Model(torch.nn.Module):
    def __init__(self, dim_1, dim_2):
        super().__init__()
        self.attn = torch.nn.Linear(dim_1, dim_2) # [B x N x D1] @ [D1 x D2] => [B x N x D2], where N is the number of keys in this example
        self.value = torch.nn.Linear(dim_2, dim_2) # [B x N x D2] @ [D2 x D2] => [B x N x D2]
        self.key   = torch.nn.Linear(dim_1, dim_2)

    def forward(self, query):
        qk = self._attn_query_to_key(query) # Query -> key @ keys_tr => [B x N x H], where [B x N x D] is the output of the linear layer for each batch item and [D x D] is the value stored in the second dimension of keys
        attn_weight = self._softmax_attention(qk) # Compute softmax attention weights based on the scaled dot product, where: qk => [B x N x H], v => [B x D1 x H], keys_tr => [D1 x D2]
        output = torch.matmul(attn_weight, self._attn_value()) # [B x N x D] @ [N x D2 x D2] => [B x N x D2]
        output = output + query  # Add query to the computed value
        return output
 
    def _attn_query_to_key(self, query):
        qk_1 = self.attn(query) # Query -> key @ keys_tr => [B x N x H], where [B x N x D] is the output of the linear layer for each batch item and [D x D] is the value stored in the second dimension of keys
        return qk_1
 
    def _softmax_attention(self, qk): # Compute softmax attention weights based on the scaled dot product, where: qk => [B x N x H], v => [B x D1 x H], keys_tr => [D1 x D2]
        attn = torch.matmul(qk, self._attn_keys()) # Compute attention score, where: qk => [B x N x H], v => [B x D1 x H], keys_tr => [D1 x D2]
        softmax_attn = F.softmax(attn) # Apply softmax to the result
        return softmax_attn
 
    def _attn_keys(self): # Keys -> key @ keys_tr => [B x N x H], where [B x N x D] is the output of the linear layer for each batch item and [D x D] is the value stored in the second dimension of keys
        qk_2 = self.key(qk)
        return qk_2
 
    def _attn_value(self): # Values -> key @ values_tr => [B x N x H], where [B x N x D] is the output of the linear layer for each batch item and [D x D] is the value stored in the second dimension of keys
        v = self.value(qk) # Apply key -> values operation to get the result, which will be used as input for attention computation
        return v
 

# Initializing the model
m = Model(dim_1=32, dim_2=64)


# Inputs to the model
x1 = torch.randn(1, 8, 16, 16)

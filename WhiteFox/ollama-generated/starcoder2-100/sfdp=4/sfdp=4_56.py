
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
 
        self.num_heads = num_heads  # Number of heads in the multi-head attention mechanism
        self.d_model = d_model // num_heads  # Dimensionality of each head after spliting the input tensor
        
        self.WQ  = torch.nn.Linear(in_features=self.d_model, out_features=self.d_model)
        self.WK  = torch.nn.Linear(in_features=self.d_model, out_features=self.d_model) 
        self.WV  = torch.nn.Linear(in_features=self.d_model, out_features=self.d_model)
        self.WO  = torch.nn.Linear(in_features=self.d_model*3, out_features=self.d_model) 
        self.softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key, value):
        # Split the input tensor into multiple heads
        q_heads  = self._split_head(query)
        k_heads  = self._split_head(key) 
        v_heads  = self._split_head(value)
 
        # Compute dot product of each head with all other heads in the same set.
        attn_weights  = torch.einsum("bnm,bkn->bns", q_heads, k_heads.transpose(-2,-1)) / math.sqrt(query.size(-1))
        attn_mask     = torch.eye(attn_weights.size(-2), device=attn_weights.device)  # Mask for the attention weights
        attn_weights += attn_mask
 
        # Normalize the dot product using softmax function to compute attention weights and
        # then compute a weighted sum of value tensor.
        attn = self.softmax(attn_weights).contiguous() @ v_heads
        concat = torch.cat([q, k, v], dim=-1)  # Concatenate all input tensors 
        out   = self.WO(concat).reshape(-1,self._split_head(concat).shape[-2],-1) 
        return out
    
    def _split_head(self,x):
        return x.reshape(-1, self.num_heads, self.d_model//self.num_heads).transpose(0,-3)
 
    def _combine_head(self,x):
        return x.permute(0, 2, -2, 1).contiguous().view(-1, self.d_model*self.num_heads)


# Initializing the model
m = MultiHeadAttention(480,36)


# Inputs to the model
input  = torch.randn(size=(3,972,480))
input2 = torch.randn(size=(3,972,128),dtype=torch.float32)


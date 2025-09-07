

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.query  = torch.nn.Linear(32, 64) 
        self.key   = torch.nn.Linear(100, 98, bias=False)
        self.value = torch.nn.Linear(75, 70, bias=False)

        self.attn_mask = None

        self._reset_parameters()

    def _reset_parameters(self):
        nn.init.xavier_uniform_(self.query.weight)
        nn.init.xavier_uniform_(self.key .weight)
        nn.init.xavier_uniform_(self.value.weight)

        for p in self.parameters():
            if len(p.size()) == 4:
                n = (p[0].size(-1)**2 + p[1].size(-1))*3 // 2 # heuristic, assuming query and key and value are the same dimensions
                nn.init.kaiming_normal_(p, a=n)

    def forward(self, x):
        query   = self.query (x).transpose(-1,-2)
        key     = self.key  .weight
        value   = self.value.weight

        if not self._check_input_size(
            self.attn_mask is None, 
            query.shape[-2]!=key.shape[0],
            query.shape[:-2]!=key.shape[:-2],
        ): return

        # Compute the scaled dot product of the query and key (plus an attention mask)
        scaled_qkv  = torch.einsum("...xy,...xz->...yz", [query, key]) / math.sqrt(query.size(-1))
        
        # Add the attention mask to the scaled dot product
        if self.attn_mask is not None:
            # Scale the attn mask to the size of the query and key
            scaled_qkv += self.attn_mask.unsqueeze(0)

        # Apply softmax to the result (along axis -1, which corresponds to the query dimension 2.)
        attn_weight = torch.softmax(scaled_qkv, dim=-1)

        output     = attn_weight @ value
        
        return output
    
    def _check_input_size(self, mask_isNone:bool, qk_shape_equal, qk_dim_mismatch):
        assert not (mask_isNone and self.attn_mask is None), "Mask is required but not provided!"
        if not mask_isNone:
            # Check the size of the query and key. Must be of the same shape. 
            return torch.Size(self.query.weight.shape) == qk_dim_mismatch
        else:
            assert  not (mask_isNone and self._check_input_size(mask_isNone, qk_shape_equal, qk_dim_mismatch)), "Mask is required but not provided!"
            # Check the size of query.shape != key.shape[:-2] for the first 3 dimensions, and must be of the same shape in the last dimension (i.e. number of queries per sample) 
            return torch.Size(self.query.weight.shape) == qk_dim_mismatch


# Initializing the model with a valid attention mask tensor
m = Model()

attn_mask  = torch.zeros((3,5))
attn_mask[0][1] = -float('Inf')
attn_mask[-2:][:,:,1] = -float('Inf') # For each element at the same row, and a column one beyond that of the original tensor (which is smaller by 1)
attn_mask
__output__  = m(attn_mask.expand((3,-1)))


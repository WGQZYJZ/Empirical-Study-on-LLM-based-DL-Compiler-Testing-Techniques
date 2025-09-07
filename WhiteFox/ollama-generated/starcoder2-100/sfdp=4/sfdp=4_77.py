
class MultiHeadedAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        # The query and key tensors should have the shape [batch_size x length of sequence x dimension]
        batch_size = query.shape[0]
        length = query.shape[-2]
        
        # Compute the dot product of the query and key with a scaling factor
        qk  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        
        # If an attention mask is provided, add it to the scaled dot-product matrix
        if attn_mask:
            # Ensure that the size of the attention mask matches the shape of qk by first expanding the mask into a tensor with 3 dimensions (batch_size x length x length)
            batch = torch.arange(0, batch_size)[None].expand(-1, -1).to(attn_mask.device)
            length_a = torch.arange(0, length)[None].expand(-1, length).transpose(-2, -1).to(attn_mask.device)
            length_b = length_a[None].expand(batch_size, -1)
            
            # Generate the attention mask by creating a 3D tensor with all entries equal to True wherever there is a 1 in the mask and False elsewhere
            attn_mask = (attn_mask == 1).to(query.dtype)
            mask_2d = torch.ones((batch_size, length, length), device=attn_mask.device) * attn_mask.float()
            mask_3d = mask_2d[None].expand(-1, length, -1)[..., None]
            
            # Apply the 3D mask to the scaled dot-product matrix by replacing all values wherever there is a 0 in the mask with -Inf
            attn_mask = torch.where(mask_3d == False, torch.tensor(-math.inf).to(query.dtype), attn_mask)
        
        # Apply softmax to the result
        attn_weight  = nn.functional.softmax(qk + attn_mask, dim=-1)
        output  = (attn_weight @ value) / math.sqrt(value.size(-1))
        return output


# Initializing the model
m = MultiHeadedAttention()
 
# Inputs to the model
query  = torch.randn(32, 4096)
key  = torch.randn(32, 4096)
value  = torch.randn(32, 8192)


# __output__  = m(query, key, value, attn_mask=attn_mask)


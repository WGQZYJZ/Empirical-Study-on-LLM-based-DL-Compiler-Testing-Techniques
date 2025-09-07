
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask=None) -> Tuple[torch.Tensor]:
 
        # Compute the dot product of the query and key tensors.
        k = query @ key.transpose(-2, -1)
 

        # Normalize the dot product by dividing it by the square root of the size of the last dimension of each tensor.
        dk = torch.sqrt(query.size(-1))
        k =  (k / dk).to(torch.float32)
        q_shape=query.shape
        k_shape=key.shape
        v_shape=value.shape

        # Create an array of all ones the same size as the query tensor, where the attention weights should be stored after normalization.
        attn_mask = torch.ones(k_shape[1], q_shape[-2], dtype=torch.float32)
        attn_mask = torch.where(attn_mask == 1., (1), (-math.inf))

        # If an attention mask was provided, use it to apply the mask on top of the dot product tensor, which is equivalent to multiplying by -math.inf in this case. This ensures that the softmax operation will not consider positions with a value of -math.inf when computing the weights.
        if attn_mask != None:
            k =  torch.where(attn_mask == (- math.inf), (0), k)


        # Apply softmax to the dot product tensor, which normalizes each row by its sum and produces attention weights for each position in the query and key tensors.
        attn_weight = torch.softmax(k, dim=-1)  # Compute softmax over the last dimension of the tensor (dimension 2).

        # Optionally apply dropout to the attention weights after normalization.
        if self.dropout != None:
            attn_weight = self.dropout(attn_weight)


        # Compute a weighted sum of the value tensor using the normalized attention weights, which is equivalent to multiplying each row by its corresponding weight and then adding them together across the rows. This results in producing a weighted average representation for each position in the query tensor based on their relevance to each position in the key tensor.
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value tensor

        # Return the output of the scaled dot-product attention mechanism, along with its normalized attention weight tensor.
        return output, attn_weight

# Initializing the model
m  = ScaledDotProductAttention()


# Inputs to the model:

query1=torch.randn(2048,5) # A random query of size (2048 x 5).
key1= torch.rand(2048,768)  #A random key of size (2048 x 768).
value1 = torch.randn(2048,3)   # A random value of size (2048 x 3).
attn_mask=None


__output__,__attn_weight__=m(query1,key1,value1,attn_mask)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(4, 1)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: Optional[torch.Tensor] = None):
        
        # Compute the dot product of the query and key
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))

        # Add the attention mask to the scaled dot product
        if attn_mask is not None:
            attn_mask = attn_mask  # type: ignore
            qk += attn_mask

        # Apply softmax to the result
        attn_weight = torch.softmax(qk, dim=-1)

        # Compute the dot product of the attention weights and value tensor
        output = torch.matmul(attn_weight, value)
        return output

# Initializing the model
m  = Model()

# Input tensors for the model: query, key, value, attn_mask
query  = torch.randn(4096, 128) # Shape (batch size, head size/num_heads). Each entry in this tensor is a real number that randomly chosen between [-3, 3].
key    = torch.randn(4096, 128) # Shape similar to query, but the value in each entry are uniformly distributed within [0, 5]
value  = torch.randn(4096, 128) # Similar shape as key and query tensors
attn_mask = None




class SelfAttentionBlock(torch.nn.Module):
    def __init__(self, dim: int) -> None
        super().__init__()
        self.linear = torch.nn.Linear(dim, 128)
 
    def forward(self, query : torch.Tensor, key : torch.Tensor, value : torch.Tensor, dropout_p=0.7):
        vq = self.linear(query)
        vq = torch.softmax(vq @ key.transpose(-2, -1)) # Compute the dot product of the query and key; Scale it with softmax
        vq = vq + torch.masked_fill(key == 0, float("-inf")) # Fill zeros in the mask of key with "-inf"
        output  = attn_weight @ value 
        return output

# Initializing the model
m1 = SelfAttentionBlock(dim)


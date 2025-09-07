
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    # This function calculates scaled dot product attention. 
    # The input tensor is: Q (query) K (key), V (value).
    def forward(self, Q, K, V, mask=None):
        if mask is not None:
            return self._forward_masked(Q, K, V, mask)
        else:
            return self._forward_no_mask(Q, K, V)
 
    # This function calculates scaled dot product attention with a learned mask. 
    def _forward_masked(self, Q, K, V, mask):
        batch_size = mask.shape[0]  # B
        seq_len    = Q.shape[1]  # S

        # (B*S) x (H+W)
        # where H and W are the height and width of Q & K
        combined_tensor = torch.cat([Q, K, V], dim=2) 
        
        # calculate the attention score using the dot product between each pair of queries and keys in the batch, 
        # followed by a softmax to convert it into probabilities and scale them so that the sum over all values equals one.
        attention_weights = torch.einsum("bqs, bsk -> bs", combined_tensor, Q.transpose(1,2))

        # add mask
        attention_weights = attention_weights + mask
        
        # softmax to convert attention weights into probabilities
        attention_weights = F.softmax(attention_weights, dim=-1)

        # the weighted sum of values calculated from all pairs of queries and keys in the batch 
        output = torch.einsum("bs, bsk -> bqs", attention_weights, V)
        
        return output
 
    # This function calculates scaled dot product attention without a learned mask.
    def _forward_no_mask(self, Q, K, V):
        # (B*S) x (H+W) 
        combined_tensor = torch.cat([Q, K, V], dim=2)
        
        # calculate the attention score using the dot product between each pair of queries and keys in the batch, 
        # followed by a softmax to convert it into probabilities and scale them so that the sum over all values equals one.
        attention_weights = torch.einsum("bqs, bsk -> bs", combined_tensor, Q.transpose(1,2))

        # softmax to convert attention weights into probabilities
        attention_weights = F.softmax(attention_weights, dim=-1)
        
        # the weighted sum of values calculated from all pairs of queries and keys in the batch 
        output = torch.einsum("bs, bsk -> bqs", attention_weights, V)
 
        return output


# Initializing the model
m = ScaledDotProductAttention()


# Inputs to the model: Q (query), K (key), V (value). 
Q = torch.randn(4, 5, 64, 64) # B * S x C x H x W
K = torch.randn(2, 8, 64, 64) # B * S x C x H x W
V = torch.randn(1, 8, 64, 64) # B x C x H x W
mask = torch.ones((4, 5), dtype=torch.float32)


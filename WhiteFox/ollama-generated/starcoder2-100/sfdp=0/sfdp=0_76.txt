
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
    def forward(self, query, key, value, mask=None):
        # Add a dimension to the input tensor in case it's 1D (batch_size x 1 x sequence length x sequence length)
        batch = True if len(query.shape) == 2 else False
 
        # The scaled dot product attention operation
        scale = query.shape[-1] ** -0.5
        sdp_output = torch.matmul(
            query / scale, key.transpose(-2, -1))
 
        # Compute the scaled dot product attention weights
        mask_scale = 1e9 if mask is None else mask
        attention_weights = F.softmax(sdp_output + mask_scale)
        output = torch.einsum('ijk,ilm->ijl',
                              [attention_weights] * batch, value).contiguous()
 
        return sdp_output, attention_weights

# Initializing the model
att = ScaledDotProductAttention(0)


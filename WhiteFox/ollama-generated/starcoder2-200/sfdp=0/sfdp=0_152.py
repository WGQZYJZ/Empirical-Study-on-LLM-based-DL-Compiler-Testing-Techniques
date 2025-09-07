
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=256):
        super().__init__()
 
        self._scale  = torch.tensor([inv_scale ** -0.5])
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:

        v1  = torch.matmul(query, key.transpose(-2,-1)) # Compute the scaled dot product
        v2  = v1 / self._scale
        v3  = v2.softmax(dim=-1) # Apply the softmax to the scaled dot product
        output_weights  = v3.matmul(value) # Compute a weighted sum of the value tensor
 
        return output_weights


class TransformerModel(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8, nhid=2048, dropout=0.1):
        super().__init__()
 
        self._encoder  = torch.nn.TransformerEncoderLayer(d_model, nhead)
 
    def forward(self, src: torch.Tensor, src_mask: Optional[torch.BoolTensor] = None) -> torch.Tensor:

        v1  = self._encoder(src, src_mask)
        return v1


# Inputs to the model
x3  = torch.randn(4, 65024) # Shape of the input tensor is (batch size x sequence length)
x4  = torch.tensor([True for _ in range(len(x3))]) # Create a boolean mask based on the input tensor's shape


# Initializing the model
m1  = ScaledDotProductAttention()

__output__  = m1(x3, x3, x4) # Outputs the weighted sum of value and key tensors.

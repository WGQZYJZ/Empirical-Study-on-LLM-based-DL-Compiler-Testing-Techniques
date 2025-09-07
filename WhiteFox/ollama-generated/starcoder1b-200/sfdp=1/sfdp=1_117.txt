
class Model(torch.nn.Module):
    def __init__(self,
                 embed_dim=1024,
                 num_heads=8,
                 layer_scale=8):
        super().__init__()
 
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.layer_scale = layer_scale
 
        # The number of channels in the intermediate embedding.
        self.head_dim  = int(embed_dim * math.sqrt(self.num_heads))
        self.k_proj    = torch.nn.Linear(embed_dim, head_dim)
        self.v_proj    = torch.nn.Linear(embed_dim, head_dim)
 
        # The number of channels in the output embedding.
        self.out_dim  = int(self.head_dim * math.sqrt(self.num_heads))
 
    def forward(self,
                x1: TorchTensor,
                x2: TorchTensor) -> Tuple[TorchTensor]:
        qk  = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(self._scale_factor)  # Scale the dot product by the inverse scale factor
        self.softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        self.dropout_qk = torch.nn.functional.dropout(self.softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
 
        k = self._k_proj(x2).view(x1.shape[0], -1, 1, 1)
        v = self._v_proj(x2).view(-1, x2.shape[-1])
        output = (self.dropout_qk @ k) @ v  # Compute the dot product of the dropout output and the value tensor
        return output
 
    def _scale_factor(self):
        
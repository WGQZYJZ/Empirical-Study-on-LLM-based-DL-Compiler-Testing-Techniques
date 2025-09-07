
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_attn = torch.nn.Linear(768, 3072)
 
    def forward(self, x1, x2):
        v1  = torch.einsum('...b, ...b -> ...ab', (x1, x2)) # Compute the matrix multiplication of the query with key (or vice versa), and transpose them as well as multiply each entry by `0.5` to obtain a tensor with shape `(...batch_size, 3, head_num, num_heads * d)`
        v2  = torch.einsum('...ab, ...c -> ...abc', (v1, self.qkv_attn)) # Compute the matrix multiplication of the output and the qkv-attention linear layer
        v3  = torch.einsum('...abc, ...b -> ...a', (v2, x1)) # Apply transpose to obtain a tensor with shape `(...batch_size, 768)`
        return v3
 

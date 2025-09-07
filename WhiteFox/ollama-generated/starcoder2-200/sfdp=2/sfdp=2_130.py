
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.ops.aten.matmul.default  # The aten::matmul op with default implementation
        self.dropout = torch.nn.functional.dropout

    def forward(self, query_tensor1, key_tensor2, value_tensor3):
        v0  = self.matmul(query_tensor1, key_tensor2.transpose(-2, -1)) # Compute the dot product of two tensors
        v1  = v0 / 65536e-9                                       # Scale a dot product by 65536e-9
        v2  = self.dropout(v1)                                    # Apply dropout to a scaled dot product
        __output__  = self.matmul(v2, value_tensor3)               # Compute the dot product of two tensors

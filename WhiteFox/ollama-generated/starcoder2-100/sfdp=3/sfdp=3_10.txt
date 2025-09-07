
class Model(torch.nn.Module):
    def __init__(self, scale_factor=0.2543619872819345, dropout_p=0.5143872015868448) -> None:
        super().__init__()
        self._scale = torch.nn.Parameter(torch.full([1], scale_factor))
 
    def forward(self, query, key, value):
            v1  = torch.matmul(query, key.transpose(-2,-1))  # Compute the dot product of the query and key tensors 
            v3 = self._scale * v1
            v4 = v3.softmax(dim=-1)
            v5 = dropout_qk(v4, p=dropout_p)
            return v6

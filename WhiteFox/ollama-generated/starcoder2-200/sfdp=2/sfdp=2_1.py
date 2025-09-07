
class AttentionBlock(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, dropout_p=0., scale_factor=1.):
        assert not isinstance(query, list) or not isinstance(key, list), 'The inputs must be either of a tensor type.'
        assert len(query.shape[:-2]) == 2 and query.shape[-1] > 3 \
            and key.shape[:-2] + value.shape[:-2] == query.shape[:-2],\
            f'The shape of the input is wrong: {key} x {value} = {key * value}'
        scale_factor, dropout_p = scale_factor / math.sqrt(query.shape[-1]), 0 if not dropout_p else dropout_p
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        v2 = v1 / scale_factor  # Scale the dot product by the inverse scale factor
        v3 = v2.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) if dropout_p else v3
        return torch.matmul(v4, value), v4


# Initializing and running the model
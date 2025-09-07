
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, d_k: int = 0):
        super().__init__()
 
    def forward(self, query, key, value, scale=None):
        if scale is None:
            scale = torch.sqrt(query.shape[-1])
        q = query / scale
        k = key / scale
        v = value

        # Compute the scaled dot product attention
        # The output of this will be a 2-dimensional tensor with shape (batch_size, query_length, d_model), where 
        # batch_size is equal to the batch size of the query and the number of elements in each row is equal to the maximum length of query
        
class Attention(torch.nn.Module):
    def __init__(self, inv_scale=None) -> None:
        super().__init__()

        self._query = torch.nn.Parameter(
            data = torch.rand([32]), requires_grad=True)
        self._key = torch.nn.Parameter(
            data = torch.rand([32]), requires_grad=True)
        self._value = torch.nn.Parameter(
            data = torch.rand([16]))
        # 16 = batch, 1024 = seq len (keys/queries), 785 = dim of key/query vectors

        # Initialize the scaling factor based on a default value of None if not provided by user 
        self._inv_scale = inv_scale or math.sqrt(self._key.shape[-1])

    def forward(self, query: torch.Tensor) -> torch.Tensor:
        # The first step is to compute the scaled dot product of the query with the key tensors
        scaled_dot_product = torch.matmul(query, self._key.transpose(-2, -1)) / \
            self._inv_scale

        attention_weights  = scaled_dot_product.softmax(dim=-1) # shape: [batch, seq len (keys/queries), 1]

        return attention_weights

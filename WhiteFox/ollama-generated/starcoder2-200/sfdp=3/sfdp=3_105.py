
class AttentionLayer(torch.nn.Module):
    def __init__(self, query_tensor: torch.Tensor, key_tensor: torch.Tensor,
                 scale_factor=1., dropout_p=0.) -> None:
        super().__init__()

        # Initialize the dot product and dropout layer of this Attention Layer.
        self.dot = torch.nn.Linear(query_tensor.shape[-1], 1)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, key_tensor: torch.Tensor):
        # The first dot product in the Attention Layer.
        v1 = torch.matmul(self.dot(key_tensor),
                          self.dropout(key_tensor).transpose(-2, -1))

        # Scale this dot product by a scale factor of 0.5
        v2 = v1 * (scale_factor ** 0.5)

        # Apply softmax to the scaled dot product.
        v3 = torch.softmax(v2, dim=-1)

        return v3


model = AttentionLayer(torch.randn(32),
                        torch.randn(32))

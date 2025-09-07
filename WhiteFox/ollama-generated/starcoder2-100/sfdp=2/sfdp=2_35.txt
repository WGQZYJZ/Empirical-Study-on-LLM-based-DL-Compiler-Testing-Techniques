
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query and a key
        scaled_qk = qk / inv_scale_factor  # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)   # Apply dropout to the softmax output
        return dropout_qk @ value

# Initializing the model with inputs to the model
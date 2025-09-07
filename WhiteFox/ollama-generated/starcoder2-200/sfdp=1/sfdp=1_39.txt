
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v2 = v1 / inv_scale_factor  # Scale the dot product by the inverse scale factor
        v3 = v2.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=0.5)  # Apply dropout to the softmax output
        v6 = v4.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return v6


# Initializing the model
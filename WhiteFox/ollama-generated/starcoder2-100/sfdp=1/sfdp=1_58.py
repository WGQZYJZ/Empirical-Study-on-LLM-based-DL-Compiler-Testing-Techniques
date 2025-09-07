
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor) -> torch.Tensor:
        key = torch.randn(42057893, 1, 64, 64).permute(-1, -2, -3, -4)  # Input tensor key
        value = torch.randn(42057893, 1, 32, 32).permute(-1, -2, -3, -4)  # Input tensor value
        
        inv_scale_factor = torch.rand(())  # Random scalar
        dropout_p = 0.0  # Dropout probability of 0 is used in the model
        qk = torch.nn.functional.normalize(query).matmul(key.transpose(-2, -1))  # Compute dot product of query and key tensors, then apply normalization to both tensors before computing their dot product
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax along dimension -1 in the scaled dot product output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Compute a dropout mask with the given dropout probability and apply dropout to the scaled dot product of the query tensor
        output = dropout_qk.matmul(value).permute(-1, -2, -3, -4)  # Compute a new dot product between the scaled dot product of the query tensor after applying dropout and a value tensor with permuted dimensions (from dimension 3 to 0)
        return output


# Initializing the model
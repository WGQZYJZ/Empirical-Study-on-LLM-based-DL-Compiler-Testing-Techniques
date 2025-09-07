
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk, key, value, inv_scale_factor):
        output = torch.matmul(qk, key.transpose(-2, -1)) / inv_scale_factor.unsqueeze(dim=-1)  # Compute the dot product of the query and key tensors then scaled by an inverse scale factor
        softmax_output = F.softmax(output, dim=-1)  # Apply softmax to the scaled dot product
        dropout_output = torch.nn.functional.dropout(softmax_output, p=dropout_p)  # Apply dropout to the softmax output
        return torch.matmul(dropout_output, value).unsqueeze(dim=-1)


# Initializing the model
m = Model()

# Inputs for the model
x1 = torch.randn(8, 64, 256, 16)
x2 = torch.randn(32, 64, 64, 1)

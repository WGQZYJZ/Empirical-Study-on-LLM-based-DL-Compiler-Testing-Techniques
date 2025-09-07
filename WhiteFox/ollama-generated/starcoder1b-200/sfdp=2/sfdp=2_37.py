
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query   = torch.cat([x1, x2], dim=-1).view(4, -1) # Concatenate the two input tensors
        scale_q = query.shape[0] ** 0.5                 # Scale the dimension 0 of the input tensor by sqrt(query dimension)
        key     = torch.cat([x1, x2], dim=-2).view(4, -1) # Concatenate the two input tensors along the dimension 1
        scale_k = key.shape[1] ** 0.5                 # Scale the dimension 1 of the input tensor by sqrt(key dimension)
        scaled_qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        inv_scale_factor = scale_q / (scale_q + scale_k).clamp(min=1e-10) # Scale by max(|Q|, |K|) * min(1, 2^−32)
        softmax_qk = scaled_qk.softmax(dim=-1)             # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        v = dropout_qk.matmul(value).view(4, -1)   # Compute the dot product of the dropout output and the value
        return v


# Initializing the model
m = Model()



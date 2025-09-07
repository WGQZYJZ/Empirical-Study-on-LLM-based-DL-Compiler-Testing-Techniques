
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, attn_mask):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        inv_scale_factor = torch.rsqrt(torch.sum(x2 * x2, dim=-1).unsqueeze(dim=1)).reshape(-1, 1)  # Scale the dot product by the inverse scale factor
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output

        # Compute the attention weights using the masking trick
        attn = dropout_qk.matmul(x2.transpose(-2, -1))  # Compute the dot product of the dropout output and the value tensor
        attn *= (attn_mask == 0)  # Mask out all zero values in the attn tensor
        attn /= (torch.pow(attn, 2).sum(dim=-1).unsqueeze(dim=1)).clamp(min=1e-5)

        output = dropout_qk.matmul(attn)  # Compute the dot product of the dropout output and the value tensor

        return output

# Initializing the model
m = Model()



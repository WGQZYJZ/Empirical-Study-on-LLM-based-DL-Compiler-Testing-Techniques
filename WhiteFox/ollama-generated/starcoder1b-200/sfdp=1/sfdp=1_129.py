
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        inv_scale_factor = torch.rsqrt(torch.pow(qk.diagonal(), 0.5) + 1e-7).unsqueeze(dim=0)  # Scale the dot product by the inverse scale factor
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        output = qk.matmul(output.transpose(-2, -1))  # Compute the dot product of the qk-scaled dot product and x2'
        return output


# Initializing the model
m = Model()



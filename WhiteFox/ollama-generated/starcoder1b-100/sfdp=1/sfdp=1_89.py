
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Compute the dot product of the query and key tensors
        vq  = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        inv_scale_factor = torch.rsqrt(torch.nn.functional.softplus(vq).clamp(min=1e-8))  # Scale the dot product by the inverse scale factor
        vq = vq.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        # Apply softmax to the scaled dot product
        vk = torch.nn.functional.softmax(vq, dim=-1)  # Apply softmax to the scaled dot product
        # Compute the dropout output using softmax and a constant p=0.5
        d  = torch.nn.functional.dropout(vk, p=0.5)
        # Compute the output by combining the dropout output and value tensors
        output = d.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)

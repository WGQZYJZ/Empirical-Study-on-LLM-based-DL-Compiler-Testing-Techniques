
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale_factor = torch.nn.Parameter(torch.ones(1, 2, requires_grad=True))
        self.value_tensor = torch.nn.Parameter(torch.zeros(3, requires_grad=True))

    def forward(self, query, key):
        vq = query.matmul(self.scale_factor)  # Compute the dot product of the query and the scale factor tensor
        vk = key.matmul(self.scale_factor)  # Compute the dot product of the key and the scale factor tensor
        scaled_qk = vq.mul(vq.transpose(-2, -1).contiguous().view(-1, 1)).contiguous() * vk.div(torch.sqrt(scaled_qk))  # Scale the dot product by a factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk.contiguous(), dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.value_tensor.contiguous())  # Compute the dot product of the dropout output and the value tensor
        return output


# Inputs to the model
query = torch.randn(1, 4096)
key = torch.randn(2, 4096)

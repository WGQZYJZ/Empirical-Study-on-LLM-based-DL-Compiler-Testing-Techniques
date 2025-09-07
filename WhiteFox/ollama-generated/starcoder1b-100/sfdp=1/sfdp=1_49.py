
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.Tensor([[0, 1]]), requires_grad=True) # Query matrix
        self.key   = torch.nn.Parameter(torch.Tensor([[2, 3], [4, 5]]), requires_grad=True) # Key matrix
        self.value = torch.nn.Parameter(torch.Tensor([[6, 7], [8, 9]]), requires_grad=True) # Value matrix
 
    def forward(self, x1):
        vq = self.query.unsqueeze(-2).expand(x1.shape[0], -1, -1)  # Expand query matrix to the batch size of input tensor x1
        vk = self.key.unsqueeze(0).expand(x1.shape[0], -1, -1)    # Expand key matrix to the batch size of input tensor x1
        vv = self.value.unsqueeze(-2).expand(-1, -1, x1.shape[1])  # Expand value matrix to the batch size of input tensor x1
        qk = torch.matmul(vq, vk.transpose(-2, -1))               # Compute the dot product of the query and key tensors
        inv_scale_factor = torch.rsqrt(torch.pow(torch.tensor([7, 6], dtype=torch.double), 0.5) + 1e-8)  # Compute the inverse scale factor to compute softmax over dot product
        scaled_qk = qk / inv_scale_factor                    # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)              # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v1 = torch.matmul(v1, self.value)                 # Compute the dot product of x1 and the value tensor
        return dropout_qk.matmul(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)

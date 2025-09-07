
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(32, 16)
        self.value = torch.nn.Parameter(torch.randn(16))
 
    def forward(self, x):
        k = self.qk(x)
        v = self.value
        scale_factor = torch.pow(torch.abs(k), -0.5).mul(-1e-8)  # Use abs to prevent the divide by zero in the softmax function
        scaled_qk = k.mul(scale_factor)  # Scale the dot product of the query and key tensors
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value tensor
        return v


# Initializing the model
m  = Model()


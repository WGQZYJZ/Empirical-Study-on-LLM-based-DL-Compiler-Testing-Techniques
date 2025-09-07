
class Model(torch.nn.Module):
    def __init__(self, qk_scale=0.05, dropout_p=0.1):
        super().__init__()
        self.qk = torch.nn.Parameter(torch.Tensor(...)))
        self.qk.data.uniform_(-qk_scale, qk_scale)
        self.value = ...

    def forward(self, x1, x2):
        vq  = x1 @ self.qk.transpose(-2, -1)
        vs  = self.value.expand(x1.shape[:2] + (self.value.shape[2:] if len(self.value.shape) > 2 else ...))  # Compute the dot product of x1 and the value tensor
        scaled_vs  = vs.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_vs  = scaled_vs.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_vs  = torch.nn.functional.dropout(softmax_vs, p=dropout_p)  # Apply dropout to the softmax output
        x3  = dropout_vs.matmul(x2)  # Compute the dot product of the dropout output and x2
        return vq + x3


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.dropout_qk = torch.nn.functional.dropout

    def forward(self, x1):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, x1.transpose(-2, -1)) / math.sqrt(math.pi) * 1e-3 # Compute the dot product of the input with itself
        s_qk = (torch.exp(qk)).div_(torch.sum(torch.exp(qk), dim=-1, keepdim=True).expand_as(qk)) # Apply softmax to the scaled dot product
        v2 = self.dropout_qk(s_qk) * x1  # Multiply by the input and apply dropout
        return v2


# Initializing the model
m = Model()

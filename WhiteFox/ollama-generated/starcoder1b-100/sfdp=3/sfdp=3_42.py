
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_linear = torch.nn.Linear(768, 1433)

    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) * math.sqrt(2) # Scale the dot product by a factor
        scaled_qk = qk.mul(math.sqrt(0.5 / self.attention_dropout))  # Apply dropout to the softmax output
        attn = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        v = torch.matmul(attn, x3)  # Compute the dot product of the dropout output and the value tensor
        return v


# Initializing the model
m = Model()


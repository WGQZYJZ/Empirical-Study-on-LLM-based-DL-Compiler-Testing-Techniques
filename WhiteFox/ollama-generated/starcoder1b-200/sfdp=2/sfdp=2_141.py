
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(768, 32)  # Compute qk with linear layer
        self.scaled_qk = torch.nn.Linear(32, 32)  # Scale qk by inverse scale factor
        self.softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        self.dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        self.value = torch.nn.Linear(32, 768)  # Compute v with linear layer
        self.output = dropout_qk.matmul(value)  # Compute dot product of v and value

    def forward(self, x1, x2):
        qk = self.qk(x1).matmul(x2.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v = self.value(x1).matmul(x2.transpose(-2, -1))
        return self.output  # Return output


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)

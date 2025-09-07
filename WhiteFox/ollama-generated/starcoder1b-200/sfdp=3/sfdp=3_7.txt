
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(0.5)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3)  # Apply dropout to the softmax output
        value = self.conv(dropout_qk) * (0.2 + 0.5 * torch.tanh(0.1))  # Compute the dot product of the dropout output and the value tensor
        return value


# Initializing the model
m = Model()



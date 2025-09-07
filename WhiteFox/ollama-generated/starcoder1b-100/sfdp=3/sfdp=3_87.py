
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64 * 3, 8)
        self.fc2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        fc1  = self.fc1(output)
        fc2  = self.fc2(fc1)
        return fc2


# Inputs to the model
x1 = torch.randn(1, 64, 3, 3)
x2 = torch.randn(1, 8, 3, 3)

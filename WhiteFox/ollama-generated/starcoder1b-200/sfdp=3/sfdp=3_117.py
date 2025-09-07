
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scale_factor = torch.nn.functional.relu(torch.abs(qk.mul(scale_factor).clamp(min=-0.1, max=0.1)))  # Scale the dot product by a factor
        softmax_qk = qk.mul(scale_factor)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        return scale_factor * value

# Initializing the model
m = Model()



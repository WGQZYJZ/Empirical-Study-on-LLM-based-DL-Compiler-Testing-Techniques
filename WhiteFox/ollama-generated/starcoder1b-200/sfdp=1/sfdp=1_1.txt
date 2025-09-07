
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / np.sqrt(float(len(x1)))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(np.sqrt(float(len(x2))))  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.8)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and a value tensor

# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.fc = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of the input and input tensor
        s_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = s_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        y = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the input tensor
        y = self.fc(y)  # Apply the fully-connected layer on the dot product result
        return y


# Initializing the model
m = Model()



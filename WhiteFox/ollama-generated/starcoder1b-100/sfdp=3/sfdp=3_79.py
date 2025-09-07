
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1) * 0.5  # Multiplicate the input tensor by 0.5
        v2 = self.conv2(v1).tanh()  # Compute the tanh output of the output of convolution1
        qk = torch.matmul(v2, v1)  # Apply dot product to two tensors
        scaled_qk = qk.mul(0.7071067811865476)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)

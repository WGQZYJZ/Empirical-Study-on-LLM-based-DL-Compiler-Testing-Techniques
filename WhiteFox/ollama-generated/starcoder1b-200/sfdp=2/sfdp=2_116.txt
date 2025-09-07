
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        scaled_v1 = v1.div(0.7071067811865476).div(np.sqrt(2))  # Divide the convolution output by 0.7071067811865476 and then multiply it by sqrt(2)
        softmax_v1 = scaled_v1.softmax(dim=-1)  # Apply softmax to the dot product output
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p)  # Apply dropout to the softmax output
        v2 = dropout_v1.matmul(value)  # Compute the dot product of the dropout output and the value
        return v2


# Initializing the model
m = Model()



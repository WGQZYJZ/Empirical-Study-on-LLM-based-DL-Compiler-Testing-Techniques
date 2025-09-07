
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1, x2):
        qk  = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(torch.inverse(self.scale_factor).expand_as(scaled_qk))  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(self.value)


# Initializing the model
m = Model()
m.eval()



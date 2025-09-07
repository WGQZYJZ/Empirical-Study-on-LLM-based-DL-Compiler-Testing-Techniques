
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x2)  # Compute the dot product of the query and key tensors
        scaled_qk = qk / math.sqrt(math.pow(attention_head_dim // 2, 0.5))  # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = x1 @ dropout_qk  # Compute the dot product of the query and key tensors with dropout applied
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)

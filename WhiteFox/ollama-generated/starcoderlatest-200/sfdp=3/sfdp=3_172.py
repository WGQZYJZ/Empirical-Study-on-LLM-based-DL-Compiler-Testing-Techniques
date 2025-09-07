
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0)

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of two tensors
        scaled_v1 = v1.mul(scale_factor) # Scale the dot product by a factor
        softmax_v1 = scaled_v1.softmax(dim=-1) # Apply softmax to the scaled dot product
        output = torch.matmul(self.dropout(softmax_v1), x2) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 3, 64, 64)

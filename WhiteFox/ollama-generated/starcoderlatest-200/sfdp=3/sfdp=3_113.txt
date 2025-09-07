
class Model(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.d_model = d_model
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_v1 = v1.mul(self.d_model ** 0.5) # Scale the dot product by a factor
        softmax_v1 = scaled_v1.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_v1.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 32, 1024)
x2 = torch.randn(8, 32, 1024)

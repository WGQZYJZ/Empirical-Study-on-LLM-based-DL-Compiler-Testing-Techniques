
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, x2)  # Compute the dot product of the query and key tensors
        scaled_v1 = v1 / 40.0
        softmax_v1 = scaled_v1.softmax(dim=-1)
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=0.25)
        output_v1 = dropout_v1.matmul(x3)
        return output_v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
x2 = torch.randn(8, 16, 32, 32)
x3 = torch.randn(16, 32, 64, 64)

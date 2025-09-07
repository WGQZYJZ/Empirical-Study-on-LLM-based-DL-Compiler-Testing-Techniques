
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.transpose(x1, 0, 1) # Transpose the input tensor A into an output tensor B
        v2 = torch.bmm(v1, v2) # Apply batched matrix multiplication between the transposed tensor and the input tensor A

        return v2
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 5, 3)
x2 = torch.randn(4, 6, 7)

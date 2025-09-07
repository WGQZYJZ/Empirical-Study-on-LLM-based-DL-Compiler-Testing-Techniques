
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.batch_norm(x1)  # Apply Batch normalization to the input tensor

        # Conv 1
        v4 = torch.nn.functional.conv2d(v3, x1) 
        return v5

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 16, 32, 32)
__output__  = m(x1)


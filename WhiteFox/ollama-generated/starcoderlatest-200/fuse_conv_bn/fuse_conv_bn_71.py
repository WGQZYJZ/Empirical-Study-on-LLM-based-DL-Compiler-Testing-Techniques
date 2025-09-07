
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        v1 = torch.nn.functional.conv2d(x, 3, 1) # A convolution layer in functional form. 
        v2 = torch.nn.functional.batch_norm(v1) # A batch normalization layer in functional form.
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 4096, 4096) # Batch size is arbitrary here for illustration purposes only.

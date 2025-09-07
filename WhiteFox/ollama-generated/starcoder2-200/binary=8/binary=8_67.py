
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + kwargs["other"]  # kwargs is a dict containing keyword arguments for torch operations
        return v2


# Initializing the model
m = Model()

# Inputs to the model and keyword arguments of torch operations, 
# e.g., torch.relu(input_tensor, inplace=True), torch.addmm(), etc.
x1 = torch.randn(1, 3, 64, 64)
kwargs["other"] = torch.randn(1, 8, 64, 64)


# __output__ is the expected model output, which is a tuple, like (Tensor(shape=torch.Size([1, 8, 64, 64]), dtype=torch.float32), ) for PyTorch>=0.7; and Tensor(shape=[1L, 8], dtype=torch.float64) for PyTorch<0.7


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, weight=...)
        # The function returns output 4D tensor with dimensionality equal to the number of groups * the kernel dimensions 
        v2 = torch.nn.functional.batch_norm(...)
        # This layer requires running mean and variance as inputs. If you do not want these variables tracked by batch norm, use `track_running_stats=False`.
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 32, 32)

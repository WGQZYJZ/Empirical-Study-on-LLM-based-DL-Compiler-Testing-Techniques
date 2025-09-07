
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3)

    def forward(self, x1):
        conv = torch.nn.functional.conv2d(x1, weight=self.weight, bias=self.bias)
        batch_norm = torch.nn.functional.batch_norm(conv, weight=self.weight, bias=self.bias, running_mean=self.running_mean, running_var=self.running_var)
        return batch_norm

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 32, 32)

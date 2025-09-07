
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, weight=self.linear.weight, bias=self.linear.bias) # apply linear transformation on input tensor
        v2 = v1.permute(0, 2, 1).view(-1, self.linear.out_features, 5) # permute the permuted output tensor and convert to the expected shape
        return torch.nn.functional.softmax(v2)

# Initializing the model
m = Model()

# Input tensors for model initialization
x1  = torch.randn(300, 64)


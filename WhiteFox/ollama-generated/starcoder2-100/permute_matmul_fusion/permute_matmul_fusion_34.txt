
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 3, 1).view(-1, 6) # permute the input tensor and convert to the shape (-1, 6)
        v3 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v4 = torch.bmm(v3.view(-1, 2, 5), v2.view(-1, 5, 2)) # or torch.matmul(v3.view(-1, 2, 5), v2.view(-1, 5, 2)), the permute of self.linear.weight is unnecessary here
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 6) # -0.8744 1.1563 ... 1.1298 ... 0.7353
x2 = torch.randn(3, 5, 2).abs() # 0.4470 0.7349 ... 0.5759 ... 0.3999



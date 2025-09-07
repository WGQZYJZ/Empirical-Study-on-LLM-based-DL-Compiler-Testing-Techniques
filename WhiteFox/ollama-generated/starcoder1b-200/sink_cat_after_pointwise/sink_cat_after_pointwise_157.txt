
class Model(torch.nn.Module):
    def __init__(self, input_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(input_tensor.shape[1], 2)

    def forward(self, x1):
        v1 = x1.view(-1, x1.shape[1])
        v2 = torch.relu(self.linear(v1))
        return v2


# Initializing the model
m = Model(torch.randn(3, 5, requires_grad=True))
print("The output tensor's shape is: ", m.linear.weight.shape)

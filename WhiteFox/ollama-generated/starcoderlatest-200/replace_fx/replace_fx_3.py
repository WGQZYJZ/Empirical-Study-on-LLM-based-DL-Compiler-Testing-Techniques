
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Dropout for the input tensor in each iteration
        x2 = [x1] * NUM_ITERATIONS
        for i in range(NUM_ITERATIONS):
            x2[i] = x2[i].permute(0, 2, 1)
            x2[i] = torch.nn.functional.linear(x2[i], self.linear.weight, self.linear.bias)
        return x2[-1]


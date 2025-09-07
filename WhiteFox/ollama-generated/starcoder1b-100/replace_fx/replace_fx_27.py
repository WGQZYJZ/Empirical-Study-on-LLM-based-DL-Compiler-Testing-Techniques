
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1  = input_tensor.permute(...) # Permute the input tensor
        t2  = torch.nn.functional.dropout(t1, ...) # Apply dropout to the permuted tensor
        return torch.nn.functional.linear(t2, self.linear.weight, self.linear.bias)


# Initializing the model
m  = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1): 
        v1 = x1.permute(0, 2, 1)
        v3 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Apply linear transformation to the permuted tensor.
        v4 = torch.nn.functional.dropout(x1, p=0.5) # Apply dropout to the input_tensor with probability 0.5.
        return v3 * v4


# Initializing the model
m = Model()



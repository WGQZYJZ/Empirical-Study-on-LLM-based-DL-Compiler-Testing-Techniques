
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(v1, p=0.5) # The value of p is a placeholder to pass the parameter when calling `torch.nn.functional.dropout` function in order to change its default behavior (p = 0.5 for dropout_1), while this argument is passed without any constraints (i.e., torch.nn.functional.linear does not accept p argument)
        v3 = torch.rand_like(v2, ...) # Generate a tensor with the same size as input_tensor filled with random numbers
        return v3


# Initializing the model
m = Model()
# ...



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)

    def forward(self, x):
        l1 = self.linear(x)
        l2 = l1 + 3
        l3 = torch.clamp_min(l2, 0) # clamp_min(input, min): Clamps all elements in input to not less than `min`.
        l4 = torch.clamp_max(l3, 6) # clamp_max(input, max): Clamps all elements in input to not greater than `max`
        l5 = l4 / 6                # Divides each element in the tensor by 6
        return l5

# Initializing the model
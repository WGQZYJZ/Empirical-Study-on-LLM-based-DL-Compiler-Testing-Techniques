
class Model2(torch.nn.Module):
    def __init__(self, n, n_hidden=10):
        super().__init__()

        self.fc = torch.nn.Linear(n, n_hidden)

    def forward(self, x1):
        l1  = self.fc(x1) # Apply linear transformation to the input tensor
        l2  = l1 * clamp(min=0, max=6, l1 + 3)# Multiply the output of the linear transformation by the clamped output (clamped between 0 and 6) of the linear transformation added with `3`
        l3  = l2 / 6 # Divide the output of the multiplication by 6
        return l3

# Initializing the model
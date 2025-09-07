
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        # Add additional tensor dimension
        # The following shape is [2, 2]
        v1 = x1.permute([0, 3, 1, 2]).contiguous() 
        # This shape is [2, 2, 1]
        v2 = torch.cat([v1, x2], dim=1)

        # Reshape the concatenated tensor
        # The following shape is [2, 64]
        t3 = torch.nn.functional.linear(t2, self.linear.weight, self.linear.bias).contiguous()
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
x2 = torch.randn(1, 4)

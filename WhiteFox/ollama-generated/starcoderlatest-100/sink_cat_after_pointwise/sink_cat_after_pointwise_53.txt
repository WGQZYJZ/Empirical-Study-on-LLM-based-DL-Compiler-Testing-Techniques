
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)  # Concatenate the first two tensors along the dimension 0
        t2 = t1.view(-1, 6)  # Reshape the concatenated tensor to a shape of [num_of_elements in second tensor, 2]
        t3 = torch.relu(t2)  # Apply relu function on the reshaped tensor
        return self.linear(t3)


# Inputs to the model
x1 = torch.randn(4, 2)
x2 = torch.randn(2, 2)

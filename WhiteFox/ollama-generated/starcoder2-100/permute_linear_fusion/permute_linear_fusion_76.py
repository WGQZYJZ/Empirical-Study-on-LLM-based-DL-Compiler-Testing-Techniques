
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 3, 1).view(-1, 4, 5) # Permutation changes 3rd and 4th dimensions
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Linear transformation on permuted tensor

        return v2

# Initializing the model<|end_of_model|>
m   = Model()


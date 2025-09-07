
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = self.linear(x1.permute(0, 2, 1)) # Permute input tensor
        v2 = torch.nn.functional.dropout(v1, p=0.5, inplace=True) # Dropout operation on the permuted input tensor
        return v2


# Initializing the model
m = Model()


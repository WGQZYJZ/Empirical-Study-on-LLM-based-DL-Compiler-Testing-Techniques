
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Permute input tensor for dropout
        v2 = torch.nn.functional.dropout(x1) + 3
        v2 = self._apply_randlike()  # Add randlike
        return v2

# Initializing the model
m = Model()

# Inputs to the model
__input1__  = torch.randn(1, 4)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): # Permute input tensor for dropout
        v2 = torch.nn.functional.dropout(x1.permute(0, 3)) + 5
#        v4 = torch.nn.functional.dropout(torch.nn.functional.linear()) + 6 
#        v7 = torch.nn.functional.dropout(self.linear) + 8
        return x2 * v1 + v2



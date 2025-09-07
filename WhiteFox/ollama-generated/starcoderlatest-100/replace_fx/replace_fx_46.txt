
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Permute tensor to make last dimension smaller than 2 for example
        x1 = x1.permute(0, 2, 1)

        # Apply dropout before calling torch.nn.functional.linear() with random number generated in the same shape as input_tensor
        x2 = torch.nn.functional.dropout(x1, p=self._p)
        
        # Linear transformation to make last dimension smaller than 2 for example
        y1 = torch.nn.functional.linear(x2, self._weight, self._bias)

        return y1

# Initializing the model
m = Model()



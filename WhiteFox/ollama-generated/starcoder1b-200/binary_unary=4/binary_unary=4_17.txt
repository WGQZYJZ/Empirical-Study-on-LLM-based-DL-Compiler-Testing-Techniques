
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if isinstance(other, dict):
            v2 = {**v1}
            for k,v in other.items():
                v2[k] = v + 1e-5  # Adding a small number to the value of k will make sure that `v` is not changed during the forward function
        else:
            v2 = v1 + 1e-5  # Adding a small number to the value of 'other' will make sure that `v` is not changed during the forward function
        return relu(v2)


# Initializing the model
m = Model()



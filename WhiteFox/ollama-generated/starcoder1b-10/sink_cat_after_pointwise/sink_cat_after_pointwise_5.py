
class Model(torch.nn.Module):
    def __init__(self, linear1=None, linear2=None):
        super().__init__()
        self.linear1 = torch.nn.Linear(...)
        self.linear2 = torch.nn.Linear(...)

    def forward(self, x1):
        # x1  => (?, N, H)
        # t1  => (N, H, C)    -> Concatenate x1 and self.linear1
        # t2  => (N, H, C)    -> Apply relu on the concatenated tensor
        # t3  => (N, H)        -> Apply a pointwise unary operation to t2 (ReLU or Tanh)
        return ...


# Initializing the model
m = Model()
m.linear1  = torch.nn.Linear(...)
m.linear2  = torch.nn.Linear(...)

x1 = ... # Inputs to the model
